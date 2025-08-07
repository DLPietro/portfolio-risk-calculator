# risk_calculator.py
# Portfolio Risk Calculator - Model 1: Historical Risk Metrics

pip install yfinance pandas numpy matplotlib
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =======================
# CONFIGURATION
# =======================
TICKERS = ["IVV", "FCNTX", "^GSPC"]  # Can be extended
WEIGHTS = [0.6, 0.4, 0.0]           # Portfolio weights (IVV 60%, FCNTX 40%)
RISK_FREE_RATE = 0.02               # 2% annual risk-free rate
CONFIDENCE_LEVEL = 0.95             # For CVaR
DAYS_PER_YEAR = 252

# =======================
# DOWNLOAD DATA
# =======================
def download_data(tickers, period="5y"):
    """Download adjusted closing prices for tickers"""
    data = yf.download(tickers, period=period)["Adj Close"]
    returns = data.pct_change().dropna()
    print(f"Downloaded {len(returns)} days of data for {tickers}")
    return returns

# =======================
# RISK METRICS
# =======================
def annualized_return(returns):
    return np.mean(returns) * DAYS_PER_YEAR

def annualized_volatility(returns):
    return np.std(returns) * np.sqrt(DAYS_PER_YEAR)

def sharpe_ratio(returns, rf=0.02):
    r = annualized_return(returns)
    vol = annualized_volatility(returns)
    return (r - rf) / vol if vol != 0 else 0

def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.expanding().max()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()

def historical_cvar(returns, alpha=0.95):
    sorted_returns = np.sort(returns)
    index = int((1 - alpha) * len(sorted_returns))
    return np.mean(sorted_returns[:index]) * np.sqrt(DAYS_PER_YEAR)  # Annualized

# =======================
# PORTFOLIO CALCULATION
# =======================
def portfolio_metrics(weights, returns, rf=0.02):
    portfolio_returns = (returns * weights).sum(axis=1)
    
    metrics = {
        "Annualized Return": f"{annualized_return(portfolio_returns):.2%}",
        "Volatility": f"{annualized_volatility(portfolio_returns):.2%}",
        "Sharpe Ratio": f"{sharpe_ratio(portfolio_returns, rf):.2f}",
        "Max Drawdown": f"{max_drawdown(portfolio_returns):.2%}",
        "Historical CVaR (95%)": f"{historical_cvar(portfolio_returns, CONFIDENCE_LEVEL):.2%}"
    }
    return metrics, portfolio_returns

# =======================
# MAIN EXECUTION
# =======================
if __name__ == "__main__":
    # Download data
    returns = download_data(TICKERS)
    
    # Select only IVV and FCNTX for portfolio
    portfolio_returns_df = returns[["IVV", "FCNTX"]]
    
    # Calculate metrics
    metrics, portfolio_rets = portfolio_metrics(WEIGHTS[:2], portfolio_returns_df, RISK_FREE_RATE)
    
    # Display results
    print("\n" + "="*50)
    print("PORTFOLIO RISK METRICS (HISTORICAL)")
    print("="*50)
    for key, value in metrics.items():
        print(f"{key:25} {value}")
    print("="*50)
    
    # Optional: Plot cumulative returns
    (1 + portfolio_rets).cumprod().plot(title="Portfolio Cumulative Returns")
    plt.ylabel("Growth of $1")
    plt.xlabel("Date")
    plt.grid(True)
    plt.show()
