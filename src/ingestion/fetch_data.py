import os
import requests
from src.utils.helpers import setup_logger

logger = setup_logger(__name__)

RAW_DIR = "data/raw"
URL = "http://url-para-dados.csv"
FILENAME = "dataset.csv"

def fetch_and_save_data():
    logger.info(f"Baixando dados de {URL}")
    response = requests(URL)
    response.raise_for_status()

    os.makedirs(RAW_DIR, exist_ok=True)
    file_path = os.path.join(RAW_DIR, FILENAME)

    with open(file_path, "wb") as f:
        f.write(response.content)

    logger.info(f"Arquivo salvo em {file_path}")
    return file_path

if __name__ == "__main__":
    fetch_and_save_data()