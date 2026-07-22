import pandas as pd
import numpy as np
from features.indicators import *

def rsi_strategy(df):
    df = calculate_rsi(df)

    df['RSI_Signal'] = np.nan
    df.loc[
        (df['rsi'] > 30) &
        (df['rsi'].shift(1) <= 30),
        'RSI_Signal'
    ] = 1

