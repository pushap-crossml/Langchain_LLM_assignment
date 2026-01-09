"""
client.py

Initializes a Google Gemini chat model client for LangChain usage. This module
creates a `ChatGoogleGenerativeAI` instance with controlled response behavior 
and exports it as `model` for use across the application.

Configuration:
- `temperature`, `top_p`, and `top_k` govern response randomness and creativity.
- `max_output_tokens` limits the number of tokens in each model output.

Security:
- Keep the API key outside of source control, e.g., via environment variables 
  or a separate secrets/credentials file not committed to the repository.

Usage:
    from client import model
    response = model.predict("Hello, world!")
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from cred import gemini_api_key
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

logger.info("Initializing Gemini chat model client")

try:
    model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        api_key=gemini_api_key,
        temperature=0.2,          # Low randomness for stable responses
        top_p=0.9,                 # Probability mass for nucleus sampling
        top_k=40,                  # Limits tokens considered at each step
        max_output_tokens=512,     # Cap on output length
    )
    logger.info("Gemini model initialized successfully")
    logger.debug(
        "Model config: model=gemini-2.5-flash-lite, "
        "temperature=0.2, top_p=0.9, top_k=40, max_output_tokens=512"
    )
except Exception as e:
    logger.error(f"Failed to initialize Gemini model: {str(e)}", exc_info=True)
    raise
