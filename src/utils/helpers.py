import logging
import os
from datetime import datetime

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Diretório para logs
        os.makedirs("logs", exist_ok=True)
        log_filename = datetime.now().strftime("logs/log_%Y-%m-%d.log")

        # Handler para console
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_formatter)

        # Handler para arquivo
        file_handler = logging.FileHandler(log_filename)
        file_formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        # Adiciona os handlers ao logger
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger
