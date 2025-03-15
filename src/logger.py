import logging
import os
from datetime import datetime 

# Define logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Ensure only the directory is created

# Define log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set logging level

# Create FileHandler
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create StreamHandler (for console output)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Testing
if __name__ == "__main__":
    logger.info("Logging has started")
