import pandas as pd
import numpy as np

def annualized_return(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Calculates the annualized compounded return (CAGR)."""
    compounded_growth = (1 + returns).prod()
    n_periods = len(returns)
    if n_periods == 0:
        return 0.0
    return (compounded_growth ** (periods_per_year / n_periods)) - 1


def annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Calculates annualized volatility (standard deviation)."""
    return returns.std() * np.sqrt(periods_per_year)


def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0, periods_per_year: int = 252) -> float:
    """Calculates the annualized Sharpe ratio."""
    vol = annualized_volatility(returns, periods_per_year)
    if vol == 0:
        return 0.0
    ann_ret = annualized_return(returns, periods_per_year)
    return (ann_ret - risk_free_rate) / vol


def max_drawdown(returns: pd.Series) -> float:
    """Calculates maximum drawdown (returned as a negative float, e.g. -0.15 for -15%)."""
    cum_returns = (1 + returns).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    return drawdown.min()


def calmar_ratio(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Calculates the Calmar ratio (Annualized Return / Absolute Max Drawdown)."""
    mdd = abs(max_drawdown(returns))
    if mdd == 0:
        return 0.0
    ann_ret = annualized_return(returns, periods_per_year)
    return ann_ret / mdd

def win_rate(returns: pd.Series) -> float:
    """Calculates the win rate (percentage of winning periods/trades)."""
    # Exclude neutral/zero return periods to focus on active trades
    active_returns = returns[returns != 0]
    if len(active_returns) == 0:
        return 0.0
    
    winning_trades = (active_returns > 0).sum()
    return winning_trades / len(active_returns)

def profit_factor(returns: pd.Series) -> float:
    """
    Calculates the Profit Factor (Gross Profits / Gross Losses).
    Returns float('inf') if there are zero losses.
    """
    gross_profits = returns[returns > 0].sum()
    gross_losses = abs(returns[returns < 0].sum())
    
    if gross_losses == 0:
        return float('inf') if gross_profits > 0 else 0.0
        
    return gross_profits / gross_losses