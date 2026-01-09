"""
agent.py

Defines a LangChain agent powered by a Google Gemini chat model that can 
call a set of tools iteratively until it generates a final response 
or reaches a stop/iteration limit.

This module integrates:
- A Google Gemini chat model (via `client.model`).
- A system prompt (from `prompt.system_prompt`) that configures agent behavior.
- A collection of tools (from `tools.*`) available for agent use.

Usage:
    from agent import agent

    # Example invocation (LangChain v1 agents expect a "messages" state):
    result = agent.invoke({
        "messages": [{"role": "user", "content": "What's the weather in Gurugram?"}]
    })

Guidelines:
- Each tool should include type hints and a concise docstring, 
  since the agent/model relies on this metadata.
- Logging is configured via `logger_config` to track agent events.
"""
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from client import model
from prompt import system_prompt
from tools import math_calculator, date_utility_tool, get_weather, analyze_text
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

logger.info("Initializing LangChain agent")

# List of tools the agent can call
tools = [math_calculator, date_utility_tool, get_weather, analyze_text]

logger.debug(f"Registered tools: {[tool.name for tool in tools]}")

try:
    agent = create_agent(
        model=model,
        tools=tools,
    )
    logger.info("Agent created successfully")
except Exception as e:
    logger.error(f"Failed to create agent: {str(e)}", exc_info=True)
    raise
