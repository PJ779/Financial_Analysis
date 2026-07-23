import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from .components import add_line

def add_bollinger_bands(
    fig,
    df,
    middle_col="middle_band",
    upper_col="upper_band",
    lower_col="lower_band",
):
    """
    Add Bollinger Bands to an existing Plotly figure.
    """

    # Middle Band
    add_line(fig, df.index, df[middle_col], "Middle", color="blue")

    add_line(fig, df.index, df[upper_col], "Upper", color="orange")
    add_line(fig, df.index, df[lower_col], "Lower Band",color="orange", fill="tonexty",
            fillcolor="rgba(255,165,0,0.2)",)

    return fig

def add_rsi(fig, df):
    add_line(fig, x=df.index, y=df['rsi'], name='RSI', color="purple")
    return fig


def add_macd(fig, df):
    # MACD and Signal lines
    add_line(fig, df.index, df["macd"], "MACD", color="blue",)
    add_line(fig, df.index, df["Signal_line"], "Signal",color="red",)
    # Histogram
    fig.add_trace(go.Bar(
        x=df.index,
        y=df['macd_histogram'],
        name='Histogram',
        marker_color=['darkgreen' if val >= 0 else 'darkred' for val in df['macd_histogram']],
        opacity=0.7  # Adjust opacity to make the bars slightly more transparent (or remove this line if you want solid color)
    ))

    return fig


def add_moving_average(fig, df):
    add_line(fig, df.index, df["MA_FAST"], "MA_FAST", color="blue")
    add_line(fig, df.index, df["MA_SLOW"], "MA_SLOW",color="red")

    return fig

def add_obv(fig, df):
    add_line(fig, df.index, df["OBV"], "OBV" ,color="purple")

    return fig

def add_vroc(fig, df):
    add_line(fig, df.index, df["VROC"], "VROC",color="purple")

    return fig

def add_adx(fig, df):

    add_line(fig, df.index,df["ADX"], "ADX", color="green")
    add_line(fig, df.index, df["+DI"], "+DI",color="blue")

    add_line(fig, df.index, df["-DI"], "-DI", color="red")

    add_line(fig, df.index, [25] * len(df),"Threshold",color="black", dash="dash", width=1)

    return fig

def add_pvt(fig, df):
    add_line(fig, df.index, df["PVT"], "PVT",color="purple")
    add_line(fig, df.index, df["Signal Line_PVT"], "Signal Line",color="red")

    return fig


def add_stochastic(fig, df):
    add_line(fig, df.index, df["%K"], "Fast Stochastic", color="green")
    add_line(fig, df.index, df["%D"], "Slow Stochastic",color="red",)

    return fig