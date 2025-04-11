from src.ingestion.fetch_data import fetch_stock_data, save_raw_data
from src.utils.helpers import setup_logger

def main():
    logger = setup_logger("main_logger")

    # Lista de ações que serão consultadas
    tickers = ["ITUB4", "PETR4", "VALE3", "CESP6", "KLBN11", "TAEE11"]
    logger.info("Iniciando coleta de dados do Yahoo Finance...")

    try:
        data = fetch_stock_data(tickers)
        logger.info(f"Dados coletados para {len(data)} ações.")

        # Mostra uma previa dos dados coletados
        sample_ticker = "PETR4.SA"
        if sample_ticker in data:
            print(f"\nPrévia dos dados para {sample_ticker}:\n", data[sample_ticker].head())

        save_raw_data(data)
        logger.info("Dados salvo com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao executar a ingestão: {e}")

if __name__ == "__main__":
    main()