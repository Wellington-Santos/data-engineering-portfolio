import logging
import os
import pandas as pd
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

def normalize_dataframe(df: pd.DataFrame, ticker: str = None) -> pd.DataFrame:
    """
    Normaliza um DataFrame para garantir consistência no projeto:
    - Remove MultiIndex nas colunas
    - Reseta o índice
    - Remove coluna 'index' se criada pelo reset_index
    - Remove nomes de índice e colunas
    - Adiciona coluna 'Ticker' (opcional)

    Parâmetros:
    - df: DataFrame de entrada
    - ticker: nome da ação (opcional)

    Retorna:
    - DataFrame normalizado
    """

    df = df.copy()

    # Remove MultiIndex (como retornando pelo yFinance)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Resetar índice e limpar nomes
    df = df.reset_index(drop = False)
    df.index.name = None
    df.columns.name = None

    # Remover coluna 'index' se existir
    if "index" in df.columns:
        df.drop(columns = ["index"], inplace = True)

    # Adicionar Ticker como coluna se fornecido
    if ticker:
        df["Ticker"] = ticker
    
    # Formatar a coluna de data
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

    return df