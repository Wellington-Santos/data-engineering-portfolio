import yfinance as yf
import pandas as pd

from datetime import datetime

def fetch_stock_data(tickers, start = "2020-01-01", end=None):

    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')
        
    data = {}
    for ticker in tickers:
        print(f"Fetching data for {ticker}")
        df = yf.download(f"{ticker}.SA", start = start, end = end)
        data[ticker] = df
    return data

def save_raw_data(data, output_dir = "data/raw"):
    for ticker, df in data.items():
        df.to_csv(f"{output_dir}/{ticker}.csv")