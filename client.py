"""
client.py
=========

Google Gemini Chat Model Client Initialization.

This module initializes and exports a configured Google Gemini chat model
(`ChatGoogleGenerativeAI`) for use with LangChain across the application.
It also optionally initializes a Mem0 memory client if a valid API key
is provided.

The exported objects from this module are intended to be imported and reused
by other modules to ensure consistent configuration and resource usage.

Exports
-------
model : ChatGoogleGenerativeAI
    A configured Gemini chat model instance with controlled generation
    parameters.
mem0 : MemoryClient or None
    An optional Mem0 memory client instance. Set to ``None`` if Mem0
    initialization fails or no API key is provided.

Configuration
-------------
The Gemini model behavior is controlled using the following parameters:
- temperature : Controls randomness of responses.
- top_p       : Enables nucleus sampling.
- top_k       : Limits candidate token selection.
- max_output_tokens : Maximum tokens per response.

Security Notes
--------------
- API keys must never be hard-coded.
- Store credentials in environment variables or a secure credentials module
  that is excluded from source control.

Example
-------
>>> from client import model
>>> response = model.predict("Hello, world!")
>>> print(response)
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from mem0 import MemoryClient

from cred import gemini_api_key, memo_api_key
from logger_config import setup_logger

# ---------------------------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------------------------

logger = setup_logger(__name__)
logger.info("Initializing Gemini chat model client")

# ---------------------------------------------------------------------------
# Gemini Model Initialization
# ---------------------------------------------------------------------------

try:
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=gemini_api_key,
        temperature=0.2,
        top_p=0.9,
        top_k=40,
        max_output_tokens=512,
    )
    logger.info("Gemini model initialized successfully")
except Exception:
    logger.error("Failed to initialize Gemini model", exc_info=True)
    raise

# ---------------------------------------------------------------------------
# Mem0 (Optional Memory Client)
# ---------------------------------------------------------------------------

mem0 = None
logger.info("Initializing Mem0 memory client")

if memo_api_key:
    try:
        mem0 = MemoryClient(api_key=memo_api_key)
        logger.info("Mem0 initialized successfully")
    except Exception:
        logger.warning(
            "Mem0 initialization failed, continuing without memory support",
            exc_info=True,
        )
else:
    logger.warning("MEMO_API_KEY not found, skipping Mem0 initialization")
