# models/ewma.py
# Exponentially Weighted Moving Average (EWMA) Volatility
# Based on RiskMetrics methodology

import numpy as np

def ewma_volatility(returns, lamb=0.94, days=252):
    """
    Calculate EWMA annualized volatility
    :param returns: pandas Series of daily returns
    :param lamb: decay factor (0.94 is standard)
    :return: annualized volatility (float)
    """
    # Initialize variance
    var = np.var(returns)  # Use sample variance as starting point
    
    # Apply EWMA recursion
    for r in returns:
        var = lamb * var + (1 - lamb) * r**2
    
    # Annualize
    return np.sqrt(var * days)
