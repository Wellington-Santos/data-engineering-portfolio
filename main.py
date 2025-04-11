from src.ingestion.fetch_data import fetch_stock_data, save_raw_data
from src.utils.helpers import setup_logger

def main():
    logger = setup_logger("main_logger")

    tickers = ["ITUB4", "PETR4.SA", "VALE3.SA", "CESP6.SA", "KLBN11.SA", "TAEE11.SA"]
    logger.info("Iniciando coleta de dados do Yahoo Finance...")

    try:
        df = fetch_stock_data(tickers)
        logger.info(f"{len(df)} registros coletados com sucesso.")
        print(df.head())
        save_raw_data(df)
        logger.info("Dados salvo com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao executar a ingestão: {e}")

if __name__ == "__main__":
    main()