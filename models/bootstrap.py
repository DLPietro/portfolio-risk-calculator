# models/bootstrap.py
# Bootstrapped Historical Simulation
# Resamples historical returns to estimate uncertainty in risk metrics

import numpy as np
import pandas as pd

def bootstrap_returns(returns, n_bootstrap=10000, random_state=None):
    """
    Bootstrap (resample with replacement) daily returns
    :param returns: pandas Series of daily portfolio returns
    :param n_bootstrap: number of bootstrap samples
    :param random_state: for reproducibility
    :return: 2D array of shape (n_bootstrap, len(returns))
    """
    if random_state:
        np.random.seed(random_state)
    
    T = len(returns)
    bootstrapped = np.random.choice(returns, size=(n_bootstrap, T), replace=True)
    return bootstrapped

def bootstrap_metric(returns, func, n_bootstrap=10000, random_state=None):
    """
    Bootstrap a single metric (e.g., mean, std, CVaR)
    :param returns: observed returns
    :param func: function to apply (e.g., lambda x: np.mean(x)*252)
    :param n_bootstrap: number of bootstrap samples
    :param random_state: seed
    :return: array of bootstrapped metric values
    """
    boot_returns = bootstrap_returns(returns, n_bootstrap, random_state)
    return np.array([func(sample) for sample in boot_returns])

def bootstrap_summary(returns, n_bootstrap=10000, confidence=0.95, random_state=42):
    """
    Full bootstrap summary for key metrics
    """
    T = len(returns)
    
    # Define annualized metrics
    def annualized_return(sample): return np.mean(sample) * 252
    def annualized_vol(sample): return np.std(sample) * np.sqrt(252)
    def sharpe_ratio(sample, rf=0.02/252): 
        r = np.mean(sample) * 252
        vol = np.std(sample) * np.sqrt(252)
        return (r - rf*252) / vol if vol > 0 else 0
    def historical_cvar(sample, alpha=0.05):
        return np.mean(np.sort(sample)[:int(alpha*len(sample))]) * np.sqrt(252)

    # Bootstrap each metric
    boot_returns = bootstrap_returns(returns, n_bootstrap, random_state)
    
    boot_metrics = {
        "Annualized Return": [annualized_return(sample) for sample in boot_returns],
        "Volatility": [annualized_vol(sample) for sample in boot_returns],
        "Sharpe Ratio": [sharpe_ratio(sample) for sample in boot_returns],
        "Historical CVaR (95%)": [historical_cvar(sample) for sample in boot_returns]
    }
    
    # Summarize
    summary = {}
    for name, values in boot_metrics.items():
        mean_val = np.mean(values)
        std_val = np.std(values)
        lower = np.percentile(values, (1-confidence)/2 * 100)
        upper = np.percentile(values, (1+(confidence))/2 * 100)
        summary[name] = {
            "Mean": f"{mean_val:.2%}",
            "Std": f"{std_val:.2%}",
            "95% CI": f"[{lower:.2%}, {upper:.2%}]"
        }
    
    return summary
