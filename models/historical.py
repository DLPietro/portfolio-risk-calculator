# models/historical.py
# Historical Risk Metrics (Volatility, CVaR, etc.)

import numpy as np

def annualized_return(returns, days=252):
    return np.mean(returns) * days

def annualized_volatility(returns, days=252):
    return np.std(returns) * np.sqrt(days)

def sharpe_ratio(returns, rf=0.02, days=252):
    r = annualized_return(returns, days)
    vol = annualized_volatility(returns, days)
    return (r - rf) / vol if vol != 0 else 0

def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.expanding().max()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()

def historical_cvar(returns, alpha=0.95, days=252):
    sorted_returns = np.sort(returns)
    index = int((1 - alpha) * len(sorted_returns))
    return np.mean(sorted_returns[:index]) * np.sqrt(days)
