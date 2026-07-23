
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from visualization.indicators import *
from .components import add_horizontal_line, add_candlestick, add_buy_markers, add_sell_markers

def plot_rsi_strategy(df):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        subplot_titles=("Price", "RSI"),
    )
    fig = add_candlestick(fig, df)
    fig = add_rsi(fig, df)

    add_horizontal_line(fig, df.index, 70, "Overbought", row=2, col=1)
    add_horizontal_line(fig, df.index, 30, "Oversold", row=2, col=1)

    fig.update_layout(
        template="plotly_dark",
        height=800,
        xaxis_rangeslider_visible=False,
    )

    return fig

def plot_adx_strategy(df):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        subplot_titles=("Price", "ADX"),
    )

    add_candlestick(fig, df)
    add_adx(fig, df)

    fig.update_layout(
        template="plotly_dark",
        height=800,
        xaxis_rangeslider_visible=False,
    )

    return fig

def plot_macd_strategy(df):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        subplot_titles=("Price", "MACD"),
    )

    add_candlestick(fig, df)
    add_macd(fig, df)

    fig.update_layout(
        template="plotly_dark",
        height=800,
        xaxis_rangeslider_visible=False,
    )

    return fig

def plot_pvt_strategy(df):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        subplot_titles=("Price", "PVT"),
    )

    add_candlestick(fig, df)
    add_pvt(fig, df)

    fig.update_layout(
        template="plotly_dark",
        height=800,
        xaxis_rangeslider_visible=False,
    )

    return fig

def plot_stochastic_oscillator_strategy(df):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        subplot_titles=("Price", "Stochastic Oscillator"),
    )

    add_candlestick(fig, df)
    add_stochastic(fig, df)

    fig.update_layout(
        template="plotly_dark",
        height=800,
        xaxis_rangeslider_visible=False,
    )

    return fig

def plot_ma_crossing_strategy(df):
    fig = go.Figure()

    add_candlestick(fig, df)
    add_moving_average(fig, df)

    add_buy_markers(
        fig,
        df,
        signal_col="Position",
    )

    add_sell_markers(
        fig,
        df,
        signal_col="Position",
    )

    fig.update_layout(
        template="plotly_dark",
        height=700,
        xaxis_rangeslider_visible=False,
    )

    return fig
