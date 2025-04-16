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

def add_moving_averages(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona colunas de médias móveis de 7 e 21 dias.
    """
    df = df.copy()

    if "Close" not in df.columns:
        raise ValueError("A coluna 'Close' é obrigatória para calcular médias móveis.")
    
    df["MM7"] = df["Close"].rolling(window=7).mean().fillna(0.0).round(2)
    df["MM21"] = df["Close"].rolling(window=21).mean().fillna(0.0).round(2)

    return df

def flag_price_drop(df: pd.DataFrame, threshold: float = -5.0) -> pd.DataFrame:
    """
    Marca dias com quedas acima do limite definido (ex: -5%)
    
    Cria coluna 'Alert_Flag' com True ou False. 
    """

    df = df.copy()

    if "Daily_Change_%" not in df.columns:
        raise ValueError("É necessário calcular 'Daily_Change_%' antes de aplicar flag de alerta.")
    
    df["Alert_Flag"] = df["Daily_Change_%"] < threshold
    return df