"""
cred.py
--------
Responsible for loading and validating all sensitive credentials (API keys) 
required by the application.

Best Practices:
- Do NOT hardcode credentials in source code.
- Load credentials from environment variables, optionally via a `.env` file.
- Validate that required keys exist before the application runs.
"""

import os
from dotenv import load_dotenv
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

logger.info("Starting credential loading process")

# Load environment variables from .env file (if present)
load_dotenv()
logger.debug(".env file loaded successfully")

# Load Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY", "")
logger.debug(f"GEMINI_API_KEY present: {bool(gemini_api_key)}")

# Load Weather API key
weather_api_key = os.getenv("WEATHER_API_KEY", "")
logger.debug(f"WEATHER_API_KEY present: {bool(weather_api_key)}")

# Validate that required API keys are present
if not gemini_api_key:
    logger.critical("GEMINI_API_KEY not found in .env file or environment")
    raise EnvironmentError("GEMINI_API_KEY not found in .env file or environment")

if not weather_api_key:
    logger.critical("WEATHER_API_KEY not found in .env file or environment")
    raise EnvironmentError("WEATHER_API_KEY not found in .env file or environment")

logger.info("All required API keys validated successfully")
