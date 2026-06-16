"""
Logging configuration for the Bank SMS Classifier API.
Provides structured logging for better debugging and monitoring.
"""

import logging
import sys
from config import LOG_LEVEL

# Configure logging format
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level=LOG_LEVEL,
    format=log_format,
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Get logger instance
logger = logging.getLogger(__name__)
