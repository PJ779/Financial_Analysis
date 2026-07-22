import pandas as pd
import numpy as np
from features.indicators import *


def _require_columns(df, columns):
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def rsi_strategy(df, oversold=30, overbought=70):
    """
    Generate RSI-based trading signals.

    Parameters
    ----------
    oversold : int
        RSI threshold for entering a long position.
    overbought : int
        RSI threshold for exiting a long position.
    """
    df = df.copy()
    _require_columns(df, ["rsi"])

    df['RSI_Signal'] = np.nan
    df.loc[
        (df['rsi'] > oversold) &
        (df['rsi'].shift(1) <= oversold),
        'RSI_Signal'
    ] = 1

    df.loc[
        (df['rsi'] < overbought) &
        (df['rsi'].shift(1) >= overbought),
        'RSI_Signal'
    ] = 0

    df['RSI_Signal'] = (
        df['RSI_Signal']
        .ffill()
        .fillna(0)
    )

    return df

def macd_strategy(df):
    """
    Generate macd-based trading signals.
    """
    df = df.copy()
    _require_columns(df, ["macd", "Signal_line"])
    df['macd_signal'] = np.where(df['macd'] > df['Signal_line'],1, 0)
    df['macd_position'] = df['macd_signal'].diff().fillna(df['macd_signal'].iloc[0])

    return df

def adx_strategy(df):
    """
    Generate adx-based trading signals.
    """
    df = df.copy()
    _require_columns(df, ["ADX", '+DI', 'DI'])

    df['adx_Signal'] = np.where((df['ADX'] > 25) & (df['+DI'] > df['-DI']), 1, 0)
    df['adx_Position'] = df['adx_Signal'].diff().fillna(df['adx_Signal'].iloc[0])

    return df

def pvt_strategy(df):
    """
    Generate pvt-based trading signals.
    """
    df=df.copy()
    _require_columns(df, ['PVT', 'Signal Line_PVT'])

    df['pvt_signal'] = np.where(df['PVT'] > df['Signal Line_PVT'], 1, 0)
    df['pvt_Position'] = df['pvt_signal'].diff().fillna(df['pvt_signal'].iloc[0])

    return df

def stochastic_oscillator_strategy(df):
    """
    Generate stochastic oscillator-based trading signals.
    """
    df=df.copy()
    _require_columns(df, ['%K', '%D'])

    df['SO_signal'] = np.where(df["%K"] > df["%D"], 1, 0)
    df['SO_Position'] = df['SO_signal'].diff().fillna(df['SO_signal'].iloc[0])

    return df

def ma_crossing_strategy(df):
    """
    Generate moving average crossing-based trading signals.
    """
    df=df.copy()
    _require_columns(df, ['MA_FAST', 'MA_SLOW'])

    df['Signal'] = np.where(df["MA_FAST"] > df["MA_SLOW"], 1, 0)
    df['Daily_Return'] = df['Close'].pct_change()
    df['Position'] = df['Signal'].diff().fillna(df['Signal'].iloc[0])

    return df




