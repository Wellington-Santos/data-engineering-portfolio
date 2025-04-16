import pandas as pd
from src.transformation.clean_data import clean_stock_data
from src.transformation.enrichment import (add_price_variation, add_moving_averages, flag_price_drop)

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


def test_add_price_variation():
    df = pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "Close": [100, 110, 99]
    })

    df["Date"] = pd.to_datetime(df["Date"])
    enriched = add_price_variation(df)

    assert "Daily_Change_%" in enriched.columns
    assert round(enriched["Daily_Change_%"].iloc[1], 2) == 10.0
    assert round(enriched["Daily_Change_%"].iloc[2], 2) == -10.0

def test_add_moving_averages():
    df = pd.DataFrame({
        "Close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    })

    result = add_moving_averages(df)
    assert "MM7" in result.columns
    assert "MM21" in result.columns
    assert result["MM7"].iloc[6] == round(sum([1,2,3,4,5,6,7])/7, 2)
    assert result["MM21"].iloc[6] == 0.0


def test_flag_price_drop():
    df = pd.DataFrame({
        "Daily_Change_%": [0.0, -2.0, -5.1, -6.5, 1.0]
    })

    result = flag_price_drop(df)
    assert "Alert_Flag" in result.columns
    assert result["Alert_Flag"].tolist() == [False, False, True, True, False]
