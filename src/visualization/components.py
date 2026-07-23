import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def add_candlestick(fig, df):
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price",
        )
    )

    return fig

def add_line(fig, x, y, name, color="blue", width=2, dash=None, fill=None,
    fillcolor=None,):
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=name,
            line=dict(
                color=color,
                width=width,
                dash=dash,
            ),
            fill=fill,
            fillcolor=fillcolor,
        )
    )

    return fig


import plotly.graph_objects as go


def add_buy_markers(
    fig,
    df,
    signal_col="Position",
    price_col="Close",
    buy_value=1,
):
    """
    Add buy markers to a Plotly figure.
    """

    buy = df[df[signal_col] == buy_value]

    fig.add_trace(
        go.Scatter(
            x=buy.index,
            y=buy[price_col],
            mode="markers",
            name="Buy",
            marker=dict(
                symbol="triangle-up",
                size=10,
                color="green",
            ),
        )
    )

    return fig

def add_sell_markers(
    fig,
    df,
    signal_col="Position",
    price_col="Close",
    sell_value=-1,
):
    """
    Add sell markers to a Plotly figure.
    """

    sell = df[df[signal_col] == sell_value]

    fig.add_trace(
        go.Scatter(
            x=sell.index,
            y=sell[price_col],
            mode="markers",
            name="Sell",
            marker=dict(
                symbol="triangle-down",
                size=10,
                color="red",
            ),
        )
    )

    return fig

def add_horizontal_line(
    fig,
    x,
    y,
    name,
    color="black",
    dash="dash",
):
    add_line(
        fig,
        x=x,
        y=[y] * len(x),
        name=name,
        color=color,
        dash=dash,
    )