import logging
import os
from pathlib import Path

from settings import Settings

# Ensure logs directory exists
Path("logs").mkdir(parents=True, exist_ok=True)

# Configure logger
logger = logging.getLogger(Settings.app_name)
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(Settings.logs_directory)
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Prevent duplicate handlers
if not logger.hasHandlers():
    logger.addHandler(file_handler)

# Optional: console output too
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
