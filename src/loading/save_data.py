import os
import pandas as pd
from src.utils.helpers import setup_logger, normalize_dataframe

logger = setup_logger(__name__)

def save_processed_data(df: pd.DataFrame, ticker: str, output_dir: str = "data/processed"):
    """
    Salva o DataFrame processado em formato CSV.

    Parâmetros:
    - df (DataFrame): Dados limpos e enriquecidos.
    - ticker (str): Nome da ação (usado como nome do arquivo).
    - output_dir (str): Caminho do diretório de saída.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)

        # Metodo para normalizar o dataframa antes de salvar no arquivo
        df = normalize_dataframe(df, ticker)

        file_path = os.path.join(output_dir, f"{ticker}.csv")
        df.to_csv(file_path, index = False)

        logger.info(f"Dados processados salvos em {file_path}")
    except Exception as e:
        logger.error(f"Erro ao salvar dados de {ticker}: {e}")