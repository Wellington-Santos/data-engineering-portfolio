import os
import yfinance as yf
import pandas as pd

from datetime import datetime
from src.utils.helpers import setup_logger, normalize_dataframe

logger = setup_logger(__name__)

def fetch_stock_data(tickers, start = "2020-01-01", end=None):

    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')

    logger.info(f"Iniciando a coleta de dados de {len(tickers)} ações de {start} até {end}")
    data = {}
    
    for ticker in tickers:
        try:
            logger.info(f"Baixando dados para {ticker}")
            df = yf.download(f"{ticker}.SA", start = start, end = end)
            
            if df.empty:
                logger.warning(f"Nenhum dado retornado para {ticker}")
            else:
                data[ticker] = df
                logger.info(f"{ticker} - {len(df)} registros obtidos")

        except Exception as e:
            logger.error(f"Erro ao coletar dados de {ticker}: {e}")
    return data

def save_raw_data(data, output_dir = "data/raw"):
    os.makedirs(output_dir, exist_ok=True)

    for ticker, df in data.items():
        try:
            df = normalize_dataframe(df,ticker)

            file_path = os.path.join(output_dir, f"{ticker}.csv")
            df.to_csv(file_path, index = False)

            logger.info(f"Dados brutos salvos em {file_path}")

        except Exception as e:
            logger.error(f"Erro ao salvar dados de {ticker}: {e}")