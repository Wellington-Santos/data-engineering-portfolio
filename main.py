# import pandas as pd

# from src.ingestion.fetch_data import fetch_stock_data, save_raw_data
# from src.transformation.clean_data import clean_stock_data
# from src.transformation.enrichment import add_price_variation
# from src.utils.helpers import setup_logger

# def main():
#     logger = setup_logger("main_logger")

#     # Lista de ações que serão consultadas
#     tickers = ["ITUB4", "PETR4", "VALE3", "CESP6", "KLBN11", "TAEE11"]
#     logger.info("Iniciando coleta de dados do Yahoo Finance...")

#     try:
#         # Etapa 1 - Coleta
#         raw_data = fetch_stock_data(tickers)
#         logger.info(f"{len(raw_data)} ações coletadas com sucesso.")

#         # Etapa 2 - Salvando dados brutos
#         save_raw_data(raw_data)
#         logger.info("Dados brutos salvos com sucesso.")

#         # Etapa 3 - Limpeza e transformação
#         cleaned_data = clean_stock_data(raw_data)
#         logger.info("Dados limpos com sucesso.")

#         # Exibir preview dos dados limpos
#         for ticker, df in cleaned_data.items():
#             logger.info(f"Preview de {ticker}:")
#             print(df.head())

#         # Exibi variação percentual das ações
#         for ticker, df in cleaned_data.items():
#             df = add_price_variation(df)

#             # Exibir corretamente
#             print(f"\n{ticker} - Variação Diária:\n")
#             print(df[["Ticker", "Date", "Close", "Daily_Change_%"]].head())

#     except Exception as e:
#         logger.error(f"Erro ao executar a ingestão: {e}")
        

# if __name__ == "__main__":
#     main()


import pandas as pd

from src.ingestion.fetch_data import fetch_stock_data, save_raw_data
from src.transformation.clean_data import clean_stock_data
from src.loading.save_data import save_processed_data
from src.utils.helpers import setup_logger
from src.transformation.enrichment import (add_price_variation, add_moving_averages, flag_price_drop)

def main():
    logger = setup_logger("main_logger")
    tickers = ["ITUB4", "PETR4", "VALE3", "KLBN11", "TAEE11"]

    try:
        raw_data = fetch_stock_data(tickers)
        save_raw_data(raw_data)
        cleaned_data = clean_stock_data(raw_data)

        # Exibir variação percentual das ações
        for ticker, df in cleaned_data.items():
            
            # Calcula a variação percentual diária
            df = add_price_variation(df)

            # Calcula o valor médio das ações entre 7 e 21 dias
            df = add_moving_averages(df)

            # Analise as médias diárias e aponta as quedas maiores que 5%
            df = flag_price_drop(df)

            # Salva os arquivos processados
            save_processed_data(df, ticker)

    except Exception as e:
        logger.error(f"Erro ao executar a ingestão: {e}")

if __name__ == "__main__":
    main()
