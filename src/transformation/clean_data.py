# import pandas as pd

# def clean_stock_data(raw_data: dict) -> dict:
#     """
#     Limpa e transforma os dados brutos de ações.

#     Parâmetros:
#     - raw_data (dict): Dicionário com tickers como chave e DataFrames como valor.

#     Retorna:
#     - dict: Dicionário com DataFrames limpos por ticker.
#     """
#     cleaned_data = {}

#     for ticker, df in raw_data.items():
#         if df.empty:
#             continue

#         df = df.copy()

#         # Remove a coluna "Adj Close" se ela existir
#         if "Adj Close" in df.columns:
#             df.drop(columns=["Adj Close"], inplace=True)

#         # Tratar valores nulos - aqui estamos apenas removendo linhas com NaN
#         df.dropna(inplace=True)

#         # Adicionar nome da ação como uma nova coluna
#         df["Ticker"] = ticker

#         # Resetar índice e padronizar coluna de datas
#         df.reset_index(inplace=True)
#         # df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
#         df["Date"] = pd.to_datetime(df["Date"])

#         cleaned_data[ticker] = df

#     # Alinhar as datas entre todos os DataFrames (necessário para comparativo entre ações)
#     if cleaned_data:
#         all_dates = [set(df["Date"]) for df in cleaned_data.values()]
#         common_dates = sorted(set.intersection(*all_dates))

#         for ticker, df in cleaned_data.items():
#             cleaned_data[ticker] = df[df["Date"].isin(common_dates)].reset_index(drop=True)

#     return cleaned_data


import pandas as pd

def clean_stock_data(raw_data: dict) -> dict:
    """
    Limpa e transforma os dados brutos de ações.
    Parâmetros:
    - raw_data (dict): Dicionário com tickers como chave e DataFrames como valor.
    Retorna:
    - dict: Dicionário com DataFrames limpos por ticker.
    """
    cleaned_data = {}
    for ticker, df in raw_data.items():
        if df.empty:
            continue
        df = df.copy()
        # Remove a coluna "Adj Close" se ela existir
        if "Adj Close" in df.columns:
            df.drop(columns=["Adj Close"], inplace=True)
        # Tratar valores nulos - aqui estamos apenas removendo linhas com NaN
        df.dropna(inplace=True)
        
        # Adicionar nome da ação como uma nova coluna
        df["Ticker"] = ticker
        # Resetar índice e padronizar coluna de datas
        df.reset_index(inplace=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
        cleaned_data[ticker] = df
        
    # Alinhar as datas entre todos os DataFrames (necessário para comparativo entre ações)
    if cleaned_data:
        all_dates = [set(df["Date"]) for df in cleaned_data.values()]
        if all_dates:  # Verifica se a lista não está vazia
            common_dates = sorted(set.intersection(*all_dates))
            for ticker, df in cleaned_data.items():
                cleaned_data[ticker] = df[df["Date"].isin(common_dates)].reset_index(drop=True)
                
    return cleaned_data
