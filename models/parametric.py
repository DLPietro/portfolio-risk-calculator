# models/parametric.py
# Parametric (Gaussian) CVaR

from scipy.stats import norm
import numpy as np

def parametric_cvar(returns, alpha=0.95, days=252):
    """
    Calculate Parametric CVaR assuming normal distribution
    """
    mean = np.mean(returns) * days
    std = np.std(returns) * np.sqrt(days)
    cvar = mean - (std / (1 - alpha)) * norm.pdf(norm.ppf(alpha))
    return cvar
