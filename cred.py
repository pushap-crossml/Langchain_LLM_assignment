"""
cred.py

Centralized credential management for the application.

This module is responsible for:
- Loading sensitive credentials (API keys) from environment variables
- Optionally reading values from a `.env` file
- Validating the presence of required credentials at startup
- Logging credential availability (without exposing secrets)

Security & Best Practices:
- Credentials must NEVER be hardcoded
- `.env` files should not be committed to version control
- Required credentials fail fast during application startup
- Optional credentials degrade functionality gracefully
"""

import os
from dotenv import load_dotenv
from logger_config import setup_logger

# ---------------------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------------------

logger = setup_logger(__name__)
logger.info("Starting credential loading process")

# ---------------------------------------------------------------------
# Environment Loading
# ---------------------------------------------------------------------

load_dotenv()
logger.debug(".env file loaded successfully")

# ---------------------------------------------------------------------
# API Keys
# ---------------------------------------------------------------------

# Required credentials
gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
weather_api_key: str = os.getenv("WEATHER_API_KEY", "")

# Optional credentials
memo_api_key: str = os.getenv("MEM0_API_KEY", "")

logger.debug(f"GEMINI_API_KEY present: {bool(gemini_api_key)}")
logger.debug(f"WEATHER_API_KEY present: {bool(weather_api_key)}")
logger.debug(f"MEM0_API_KEY present: {bool(memo_api_key)}")

# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

if not gemini_api_key:
    logger.critical("GEMINI_API_KEY not found in environment variables")
    raise EnvironmentError("GEMINI_API_KEY not found")

if not weather_api_key:
    logger.critical("WEATHER_API_KEY not found in environment variables")
    raise EnvironmentError("WEATHER_API_KEY not found")

# Optional dependency (do not fail application)
if not memo_api_key:
    logger.warning("MEM0_API_KEY not found; Mem0 functionality will be disabled")

logger.info("All required API keys validated successfully")

# ---------------------------------------------------------------------
# Memory Configuration
# ---------------------------------------------------------------------

#: Default user identifier for memory persistence
USER_ID: str = "Pushap"
