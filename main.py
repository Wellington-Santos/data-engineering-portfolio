from src.ingestion.fetch_data import fetch_stock_data, save_raw_data
from src.transformation.clean_data import clean_stock_data
from src.utils.helpers import setup_logger

def main():
    logger = setup_logger("main_logger")

    # Lista de ações que serão consultadas
    tickers = ["ITUB4", "PETR4", "VALE3", "CESP6", "KLBN11", "TAEE11"]
    logger.info("Iniciando coleta de dados do Yahoo Finance...")

    try:
        # Etapa 1 - Coleta
        raw_data = fetch_stock_data(tickers)
        logger.info(f"{len(raw_data)} ações coletadas com sucesso.")

        # Etapa 2 - Salvando dados brutos
        save_raw_data(raw_data)
        logger.info("Dados brutos salvos com sucesso.")

        # Etapa 3 - Limpeza e transformação
        cleaned_data = clean_stock_data(raw_data)
        logger.info("Dados limpos com sucesso.")

        # Exibir preview dos dados limpos
        for ticker, df in cleaned_data.items():
            logger.info(f"Preview de {ticker}:")
            print(df.head())

    except Exception as e:
        logger.error(f"Erro ao executar a ingestão: {e}")

if __name__ == "__main__":
    main()