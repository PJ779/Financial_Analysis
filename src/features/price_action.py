import pandas as pd
import numpy as np


def calculate_intraday_momentum(df):
    df =df.copy()
    df['intraday_momentum'] = df['Close']-df['Open']

    return df

def calculate_volume_weighted_return(df):
    df=df.copy()
     
    df['volume_weighted_return'] = df['Close'].pct_change() * df['Volume']

    return df

def calculate_close_position_in_range(df, epsilon=1e-8):
    df=df.copy()
    df['close_position_in_range'] = (df['Close'] - df['Low'])/(df['High'] - df['Low'] + epsilon)

    return df

def calculate_money_flow_volume(df, epsilon = 1e-8):
    df=df.copy()
    # Avoid division by zero by adding a tiny epsilon value to denominators

    mf_multiplier = ((df['Close'] - df['Low']) - (df['High'] - df['Close'])) / (df['High'] - df['Low'] + epsilon)
    df['money_flow_volume'] = mf_multiplier * df['Volume']

    return df

def calculate_wick_analysis(df, epsilon = 1e-8):
    df=df.copy()

    df['upper_shadow_ratio'] = (df['High'] - df[['Close', 'Open']].max(axis=1)) / (df['Close']+ epsilon)
    df['lower_shadow_ratio'] = (df[['Close', 'Open']].min(axis=1) - df['Low']) / (df['Close'] + epsilon)

    return df

def create_market_microstructure_features(df):
    df = calculate_intraday_momentum(df)
    df = calculate_volume_weighted_return(df)
    df = calculate_money_flow_volume(df)
    df = calculate_wick_analysis(df)
    df = calculate_close_position_in_range(df)

    return df