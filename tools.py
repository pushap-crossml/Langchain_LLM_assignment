import ast
import operator as op
import requests
from datetime import date, timedelta

from langchain_core.tools import tool
from cred import weather_api_key
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

# ==================== Math Tool (Safe Evaluation) ====================
OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}


def _eval_expr(node: ast.AST) -> float:
    """
    Recursively evaluates a restricted Python AST node representing an arithmetic expression.

    Args:
        node (ast.AST): AST node produced by parsing an expression.

    Returns:
        float: Computed numeric result.

    Raises:
        ValueError: If an unsupported AST node is encountered.
    """
    logger.debug(f"Evaluating AST node: {type(node).__name__}")
    
    if isinstance(node, ast.Constant):
        return node.n
    if isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](
            _eval_expr(node.left),
            _eval_expr(node.right)
        )
    
    logger.error(f"Invalid expression node type: {type(node).__name__}")
    raise ValueError("Invalid expression")


@tool
def math_calculator(expression: str) -> str:
    """
    Safely evaluates a basic arithmetic expression using AST parsing (no eval).

    Args:
        expression (str): Arithmetic expression like "(234 * 12) + 98".

    Returns:
        str: "Result: <value>" or error message if evaluation fails.
    """
    logger.info(f"[TOOL CALL] math_calculator invoked with expression: {expression}")
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval_expr(tree.body)
        logger.info(f"[TOOL SUCCESS] Math calculation result: {result}")
        return f"Result: {result}"
    except Exception as e:
        logger.error(f"[TOOL ERROR] Math calculation failed: {str(e)}", exc_info=True)
        return f"Error evaluating expression: {str(e)}"


# ==================== Text Analysis Tool ====================
@tool
def analyze_text(text: str) -> dict:
    """
    Computes word count, character count, and a simple sentiment label for input text.

    Args:
        text (str): Input text to analyze.

    Returns:
        dict: {
            "word_count": int,
            "character_count": int,
            "sentiment": str ("Positive", "Negative", or "Neutral")
        }
        On error, returns {"error": "<message>"}.
    """
    logger.info(f"[TOOL CALL] analyze_text invoked with text length: {len(text)}")
    logger.debug(f"Text preview: {text[:100]}...")

    try:
        words = text.split()
        char_count = len(text)

        positive_words = ["good", "great", "excellent", "happy", "love"]
        negative_words = ["bad", "poor", "sad", "hate", "terrible"]

        sentiment_score = sum(
            1 if w.lower() in positive_words else -1 if w.lower() in negative_words else 0
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
            "sentiment": sentiment
        }

        logger.info(f"[TOOL SUCCESS] Text analysis complete: {result}")
        return result

    except Exception as e:
        logger.error(f"[TOOL ERROR] Text analysis failed: {str(e)}", exc_info=True)
        return {"error": str(e)}


# ==================== Date Utility Tool ====================
@tool("date_utility_tool")
def date_utility_tool(days: int) -> str:
    """
    Returns the calendar date after N days from today.

    Args:
        days (int): Number of days to add to today's date.

    Returns:
        str: ISO date string "YYYY-MM-DD" or error message.
    """
    logger.info(f"[TOOL CALL] date_utility_tool invoked with days: {days}")
    
    try:
        if days is None:
            raise ValueError("Days is None.")
        if not isinstance(days, int):
            raise TypeError("Days must be an integer.")
        
        result_date = (date.today() + timedelta(days=days)).isoformat()
        logger.info(f"[TOOL SUCCESS] Calculated date: {result_date}")
        return result_date

    except Exception as e:
        logger.error(f"[TOOL ERROR] Date calculation failed: {str(e)}", exc_info=True)
        return f"ERROR: {type(e).__name__}: {e}"


# ==================== Weather Tool ====================
@tool
def get_weather(city: str) -> dict:
    """
    Fetches live weather data for a city using OpenWeatherMap API.

    Args:
        city (str): City name (e.g., "Chandigarh").

    Returns:
        dict: {
            "temperature": float (°C),
            "condition": str (description)
        }
        On failure: {"error": "<message>"}.
    """
    logger.info(f"[TOOL CALL] get_weather invoked for city: {city}")

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        logger.debug(f"Making API request to OpenWeatherMap: {url}")

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        result = {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }

        logger.info(f"[TOOL SUCCESS] Weather data retrieved: {result}")
        return result

    except requests.exceptions.Timeout:
        logger.error(f"[TOOL ERROR] Weather API request timed out for city: {city}")
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as e:
        logger.error(f"[TOOL ERROR] Weather API request failed: {str(e)}", exc_info=True)
        return {"error": str(e)}
    except Exception as e:
        logger.error(f"[TOOL ERROR] Unexpected error in get_weather: {str(e)}", exc_info=True)
        return {"error": str(e)}
