import pandas as pd
from src.transformation.clean_data import clean_stock_data

def test_clean_data():
    # Mock de um DataFrame:
    df = pd.DataFrame({
        "Open": [10, 20],
        "High": [15, 25],
        "Low": [8, 18],
        "Close": [12, 22],
        "Adj Close": [11, 21],
        "Volume": [1000, None],
    }, index=pd.to_datetime(["2024-01-01", "2024-01-02"]))

    df = df.reset_index()
    df.rename(columns={"index": "Date"}, inplace=True)  # 🔧 ESSENCIAL

    raw_data = {"TEST4": df}
    cleaned_data = clean_stock_data(raw_data)
    cleaned_df = cleaned_data["TEST4"]

    # Verificações básicas
    assert "Adj Close" not in cleaned_df.columns
    assert "Ticker" in cleaned_df.columns
    assert cleaned_df["Ticker"].unique()[0] == "TEST4"
    assert not cleaned_df.isnull().values.any()
    assert "Date" in cleaned_df.columns
    assert pd.to_datetime(cleaned_df["Date"]).dtype == "datetime64[ns]"
