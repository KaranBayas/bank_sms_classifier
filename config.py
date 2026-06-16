"""
Configuration and settings for the Bank SMS Classifier API.
Loads settings from environment variables with sensible defaults.
"""

import os
from pathlib import Path
from logging import INFO, DEBUG, WARNING, ERROR

# Paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = os.getenv("MODEL_PATH", BASE_DIR / "bank_sms_classifier.pkl")

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# API Configuration
API_TITLE = "Bank SMS Classifier API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "Classify bank transaction SMS messages into categories using ML"

# Input Validation
SMS_MIN_LENGTH = 1
SMS_MAX_LENGTH = 1000
