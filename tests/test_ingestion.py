import os
import pandas as pd
from unittest.mock import patch

from src.ingestion.fetch_data import fetch_stock_data, save_raw_data


def test_fetch_stock_data():
    tickers = ["ITUB4", "PETR4"]
    data = fetch_stock_data(tickers, start = "2023-01-01", end = "2023-01-10")
    assert len(data) == 2
    for ticker in tickers:
        assert not data[ticker].empty

def test_save_raw_data(tmp_path):
    tickers = ["ITUB4"]
    data = fetch_stock_data(tickers, start = "2023-01-01", end = "2023-01-05")
    save_raw_data(data, output_dir=tmp_path)
    for ticker in tickers:
        file_path = tmp_path / f"{ticker}.csv"
        assert file_path.exists()
        assert file_path.stat().st_size > 0

@patch("yfinance.download")
def test_fetch_stock_data_with_mock(mock_download):
    # Simula retorno de um DataFrame
    mock_df = pd.DataFrame({"Close": [10, 11]})
    mock_download.return_value = mock_df

    data = fetch_stock_data(["MOCK11"])
    assert "MOCK11" in data
    assert data["MOCK11"].equals(mock_df)