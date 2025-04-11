# import sys
import os
from src.ingestion.fetch_data import fetch_stock_data, save_raw_data

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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