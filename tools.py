"""
tools.py

Collection of LangChain-compatible tools used by the agent.

This module provides:
- A secure arithmetic calculator using restricted AST evaluation
- Text analysis utilities (word count, character count, sentiment)
- Date computation utilities
- Live weather data retrieval via external API

Design Principles:
- Tools must be deterministic and side-effect free where possible
- External API calls must be logged and time-bounded
- Errors must be handled gracefully and returned in structured form
- Unsafe operations (e.g., eval) are explicitly avoided
"""

import ast
import operator as op
import requests
from datetime import date, timedelta

from langchain_core.tools import tool
from cred import weather_api_key
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

# =====================================================================
# Math Tool (Safe Arithmetic Evaluation)
# =====================================================================

#: Mapping of allowed AST operator nodes to Python functions
OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}


def _eval_expr(node: ast.AST) -> float:
    """
    Recursively evaluate a restricted arithmetic AST node.

    Only basic arithmetic operations defined in `OPERATORS` are supported.
    This function explicitly prevents execution of arbitrary Python code
    by rejecting unsupported AST node types.

    Args:
        node (ast.AST): AST node produced by parsing an arithmetic expression.

    Returns:
        float: Computed numeric result.

    Raises:
        ValueError: If an unsupported or unsafe AST node is encountered.
    """
    logger.debug(f"Evaluating AST node: {type(node).__name__}")

    if isinstance(node, ast.Constant):
        return node.n

    if isinstance(node, ast.BinOp):
        operator_fn = OPERATORS.get(type(node.op))
        if operator_fn is None:
            raise ValueError("Unsupported operator")

        return operator_fn(
            _eval_expr(node.left),
            _eval_expr(node.right),
        )

    logger.error(f"Invalid expression node type: {type(node).__name__}")
    raise ValueError("Invalid expression")


@tool
def math_calculator(expression: str) -> str:
    """
    Safely evaluate a basic arithmetic expression.

    The expression is parsed into an AST and evaluated using a
    restricted set of operators. This approach avoids the use
    of Python's `eval` and prevents arbitrary code execution.

    Args:
        expression (str): Arithmetic expression
            (e.g., "(234 * 12) + 98").

    Returns:
        str: Result string in the format:
            - "Result: <value>" on success
            - "Error evaluating expression: <message>" on failure
    """
    logger.info(
        f"[TOOL CALL] math_calculator invoked with expression: {expression}"
    )

    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval_expr(tree.body)

        logger.info(
            f"[TOOL SUCCESS] Math calculation result: {result}"
        )
        return f"Result: {result}"

    except Exception as exc:
        logger.error(
            f"[TOOL ERROR] Math calculation failed: {exc}",
            exc_info=True,
        )
        return f"Error evaluating expression: {exc}"


# =====================================================================
# Text Analysis Tool
# =====================================================================

@tool
def analyze_text(text: str) -> dict:
    """
    Analyze text for basic statistics and sentiment.

    This tool computes:
    - Word count
    - Character count
    - A naive sentiment classification based on keyword matching

    Args:
        text (str): Input text to analyze.

    Returns:
        dict: Analysis result with keys:
            - word_count (int)
            - character_count (int)
            - sentiment (str): "Positive", "Negative", or "Neutral"

        On failure:
            {"error": "<message>"}
    """
    logger.info(
        f"[TOOL CALL] analyze_text invoked with text length: {len(text)}"
    )
    logger.debug(f"Text preview: {text[:100]}...")

    try:
        words = text.split()
        char_count = len(text)

        positive_words = {"good", "great", "excellent", "happy", "love"}
        negative_words = {"bad", "poor", "sad", "hate", "terrible"}

        sentiment_score = sum(
            1 if w.lower() in positive_words
            else -1 if w.lower() in negative_words
            else 0
            for w in words
        )

        sentiment = "Neutral"
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"

        result = {
            "word_count": len(words),
            "character_count": char_count,
            "sentiment": sentiment,
        }

        logger.info(
            f"[TOOL SUCCESS] Text analysis complete: {result}"
        )
        return result

    except Exception as exc:
        logger.error(
            f"[TOOL ERROR] Text analysis failed: {exc}",
            exc_info=True,
        )
        return {"error": str(exc)}


# =====================================================================
# Date Utility Tool
# =====================================================================

@tool("date_utility_tool")
def date_utility_tool(days: int) -> str:
    """
    Compute the calendar date after a given number of days from today.

    Args:
        days (int): Number of days to add to the current date.
            Can be positive or negative.

    Returns:
        str: ISO-formatted date string ("YYYY-MM-DD") on success.

        On failure:
            "ERROR: <ExceptionType>: <message>"
    """
    logger.info(
        f"[TOOL CALL] date_utility_tool invoked with days: {days}"
    )

    try:
        if days is None:
            raise ValueError("Days is None")
        if not isinstance(days, int):
            raise TypeError("Days must be an integer")

        result_date = (
            date.today() + timedelta(days=days)
        ).isoformat()

        logger.info(
            f"[TOOL SUCCESS] Calculated date: {result_date}"
        )
        return result_date

    except Exception as exc:
        logger.error(
            f"[TOOL ERROR] Date calculation failed: {exc}",
            exc_info=True,
        )
        return f"ERROR: {type(exc).__name__}: {exc}"


# =====================================================================
# Weather Tool
# =====================================================================

@tool
def get_weather(city: str) -> dict:
    """
    Retrieve current weather information for a city.

    Uses the OpenWeatherMap API to fetch live weather data.
    Requests are time-bounded and errors are handled gracefully.

    Args:
        city (str): City name (e.g., "Chandigarh").

    Returns:
        dict: Weather information:
            - temperature (float): Temperature in °C
            - condition (str): Weather description

        On failure:
            {"error": "<message>"}
    """
    logger.info(
        f"[TOOL CALL] get_weather invoked for city: {city}"
    )

    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={weather_api_key}&units=metric"
        )
        logger.debug(
            f"Making API request to OpenWeatherMap: {url}"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        result = {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
        }

        logger.info(
            f"[TOOL SUCCESS] Weather data retrieved: {result}"
        )
        return result

    except requests.exceptions.Timeout:
        logger.error(
            f"[TOOL ERROR] Weather API request timed out for city: {city}"
        )
        return {"error": "Request timed out"}

    except requests.exceptions.RequestException as exc:
        logger.error(
            f"[TOOL ERROR] Weather API request failed: {exc}",
            exc_info=True,
        )
        return {"error": str(exc)}

    except Exception as exc:
        logger.error(
            f"[TOOL ERROR] Unexpected error in get_weather: {exc}",
            exc_info=True,
        )
        return {"error": str(exc)}
