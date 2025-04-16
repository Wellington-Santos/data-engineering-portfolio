import pandas as pd
import logging 
from src.utils.helpers import setup_logger, normalize_dataframe

def test_setup_logger_creates_logger():
    logger = setup_logger("test_logger")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"

def test_normalize_dataframe_flatten_and_add_tricker():
    # Simula um DataFrame com MultiIndex nas colunas e índece nomeado
    columns = pd.MultiIndex.from_tuples([
        ("Open", "AAPL"), ("Close", "AAPL"), ("Volume", "AAPL")
    ])
    df = pd.DataFrame([[100, 110, 1000]], columns = columns)
    df.index.name = "Date"

    result = normalize_dataframe(df, ticker="AAPL")

    assert "Ticker" in result.columns
    assert result["Ticker"].iloc[0] == "AAPL"
    assert "index" not in result.columns
    assert isinstance(result.columns, pd.Index)