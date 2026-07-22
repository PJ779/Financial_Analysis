import yfinance as yf
import pandas as pd

from src.config import RAW_DATA


def download_stock_data(
    ticker: str,
    start_date: str,
    end_date: str
) -> pd.DataFrame:
    
        df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True
    )
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        return df


def save_raw_data(
    df: pd.DataFrame,
    filename: str
):
    
    """
    Save dataframe to data/raw.
    """
    
    path = RAW_DATA / filename

    df.to_csv(path)

    print(f"Saved to {path}")
