# import pandas as pd

# def add_price_variation(df: pd.DataFrame):
#     """
#     Adiciona a variação percentual diária da coluna 'Close' ao DataFrame.

#     Parâmetros:
#     - df (pd.DataFrame): DataFrame com coluna 'Close' e datas ordenadas.

#     Retorna:
#     - pd.DataFrame: DataFrame com nova coluna 'Daily_Change_%'
#     """

#     # df = df.copy()

#     # if "Close" not in df.columns:
#     #     raise ValueError("A coluna 'Close' é obrigatória para calcular a variação percentual.")
    
#     # df["Daily_Change_%"] = df["Close"].pct_change() * 100
#     # df["Daily_Change_%"] = df["Daily_Change_%"].round(2)

#     df = df.copy()

#     if "Close" not in df.columns:
#         raise ValueError("A coluna 'Close' é obrigatória para calcular a variação percentual.")
    
#     # Ordenar por data antes de calcular a variação
#     df['Date'] = pd.to_datetime(df['Date'])
#     df = df.sort_values(by='Date')

#     # Calcular a variação percentual e preencher NaN com 0
#     df["Daily_Change_%"] = df["Close"].pct_change().fillna(0) * 100
#     df["Daily_Change_%"] = df["Daily_Change_%"].round(2)

#     df = df.iloc[1:]

#     return df

import pandas as pd

def add_price_variation(df: pd.DataFrame):
    """
    Adiciona a variação percentual diária da coluna 'Close' ao DataFrame.
    """
    df = df.copy()
    if "Close" not in df.columns:
        raise ValueError("A coluna 'Close' é obrigatória para calcular a variação percentual.")

    df["Daily_Change_%"] = df["Close"].pct_change().fillna(0) * 100
    df["Daily_Change_%"] = df["Daily_Change_%"].round(2)

    return df
