#logging data file

import logging
import os

def logging_info():
    os.makedirs('logs', exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler('logs/scanner.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger