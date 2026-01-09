"""
logger_config.py
----------------
Centralized logging configuration for the entire project.
Provides consistent log formatting, levels, and handlers across all modules.

Features:
- Rotating file logs (5MB per file, 5 backups)
- Console logs with concise output
- Customizable logger name and log level
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from datetime import datetime


def setup_logger(name: str, log_file: str = "agent_app.log", level=logging.DEBUG) -> logging.Logger:
    """
    Creates and configures a logger with both file and console handlers.

    Args:
        name (str): Logger name (typically __name__ of the calling module)
        log_file (str): Path to the log file
        level (int): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        logging.Logger: Configured logger instance
    """
    # Create or retrieve logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent adding duplicate handlers if logger already exists
    if logger.handlers:
        return logger
    
    # Formatter for detailed file logs
    detailed_formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Formatter for concise console logs
    console_formatter = logging.Formatter(
        fmt='%(levelname)-8s | %(name)s | %(message)s'
    )
    
    # File handler with rotation (max 5MB per file, keep 5 backups)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5*1024*1024,  # 5 MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    # Console handler (INFO level by default)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    
    # Attach handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# Create a default logger for the application
app_logger = setup_logger('agent_app')
app_logger.info("="*50)
app_logger.info("Logging system initialized")
app_logger.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
app_logger.info("="*50)
