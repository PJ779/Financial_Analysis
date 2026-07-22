import numpy as np
import pandas as pd

def calculate_rsi(df, window=14):
    df = df.copy()
    delta = df['Close'].diff()
    gain = (delta.where(delta >0, 0)).rolling(window = window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain/loss
    rsi = 100 - (100/(1+ rs))
    df['rsi'] = rsi

    return df

def calculate_macd(df, fast_window=12,
    slow_window=26,
    signal_window=9,):
    df = df.copy()
    df['EMA_SLOW'] = df['Close'].ewm(span=slow_window, adjust=False).mean()
    df['EMA_FAST'] = df['Close'].ewm(span=fast_window, adjust=False).mean()
    df['macd'] = df['EMA_FAST'] - df['EMA_SLOW']
    df['Signal_line'] = df['macd'].ewm(span=signal_window, adjust=False).mean()

    return df


def calculate_bollinger(df, window=20, std_multiplier=2):
    df = df.copy()
    rolling_mean_20_day = df['Close'].rolling(window).mean()
    df['middle_band'] = rolling_mean_20_day
    rolling_std_20_days = df['Close'].rolling(window).std()
    df['upper_band'] = rolling_mean_20_day + std_multiplier * rolling_std_20_days
    df['lower_band'] = rolling_mean_20_day - std_multiplier * rolling_std_20_days
    df['above_bb_high'] = (df['Close'] >= df['upper_band']).astype(int)
    df['below_bb_low'] = (df['Close'] <= df['lower_band']).astype(int)

    return df

def calculate_adx(df, window=14):
    df = df.copy()
    df['TR'] = pd.concat([df['High'] - df['Low'],
                      (df['High'] - df['Close'].shift(1)).abs(),
                      (df['Low'] - df['Close'].shift(1)).abs()], axis=1).max(axis=1)

    df['+DM'] = np.where(df['High'] - df['High'].shift(1) > df['Low'].shift(1) - df['Low'], df['High'] - df['High'].shift(1), 0)
    df['-DM'] = np.where(df['Low'].shift(1) - df['Low'] > df['High'] - df['High'].shift(1), df['Low'].shift(1) - df['Low'], 0)

    window = 14
    df['Smoothed +DM'] = df['+DM'].rolling(window=window).sum()
    df['Smoothed -DM'] = df['-DM'].rolling(window=window).sum()
    df['Smoothed TR'] = df['TR'].rolling(window=window).sum()

    df['+DI'] = (df['Smoothed +DM'] / df['Smoothed TR']) * 100
    df['-DI'] = (df['Smoothed -DM'] / df['Smoothed TR']) * 100

# Step 5: Calculate DX
    df['DX'] = (abs(df['+DI'] - df['-DI']) / (df['+DI'] + df['-DI'])) * 100

# Step 6: Smooth DX to get ADX
    df['ADX'] = df['DX'].rolling(window=window).mean()

    return df

def calculate_obv(df):
    df = df.copy()
    direction = np.sign(df['Close'].diff()).fillna(0)
    df['OBV'] = (direction * df['Volume']).cumsum()

    return df

def calculate_pvt(df, window=9):
    df = df.copy()
    df['PVT'] = (df['Close'].pct_change() * df['Volume']).cumsum()
    df['Signal Line_PVT'] = df['PVT'].rolling(window).mean() 

    return df

def calculate_vroc(df, window=30):
    df = df.copy()
    df['VROC'] = (df['Volume'].diff(window)/df['Volume'].shift(window)) * 100

    return df

def calculate_stochastic(df, window=14):
    df = df.copy()
    df['rolling_min'] = df['Close'].rolling(window=window).min()
    df['rolling_max'] = df['Close'].rolling(window=window).max()
    df['%K'] = ((df['Close'] - df['rolling_min']) / (df['rolling_max'] - df['rolling_min'])) * 100

# Calculate %D as the 3-period simple moving average (SMA) of %K
    df['%D'] = df['%K'].rolling(window=3).mean()

    return df

def ma_crossing_strategy(df, fast_window=10, slow_window=50):
    df = df.copy()
    df["MA_FAST"] = df['Close'].rolling(window = fast_window).mean()
    df["MA_SLOW"] = df['Close'].rolling(window = slow_window).mean()

    df['Signal'] = np.where(df["MA10"] > df["MA50"], 1, 0)
    df['Daily_Return'] = df['Close'].pct_change()
    df['Position'] = df['Signal'].diff().fillna(df['Signal'].iloc[0])

    return df


def create_technical_indicators(df):
    """
    Generate all technical indicators.
    """

    df = calculate_rsi(df)
    df = calculate_macd(df)
    df = calculate_bollinger(df)
    df = calculate_adx(df)
    df = calculate_obv(df)
    df = calculate_pvt(df)
    df = calculate_vroc(df)
    df = calculate_stochastic(df)

    return df