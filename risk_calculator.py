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
TICKERS = ["SPY", "AGG", "GLD", "FXE", "EEM"]  # Sample of 5 different assets
WEIGHTS = [0.6, 0.4, 0.0]           # Portfolio weights (20% per Asset)
RISK_FREE_RATE = 0.02               # 2% annual risk-free rate
CONFIDENCE_LEVEL = 0.95             # For CVaR
DAYS_PER_YEAR = 252

# =======================
# DOWNLOAD DATA
# =======================
def download_data(tickers, period="5y"):
    """Download adjusted closing prices for tickers"""
    data = yf.download(tickers, period=period)["Adj Close"]
    
    # Forward-fill & drop remaining NaNs
    data = data.ffill().dropna()
    
    # Calculate daily returns
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
# INDIVIDUAL ASSET ANALYSIS
# =======================
def display_asset_metrics(returns, weights):
    print("\n" + "="*60)
    print("INDIVIDUAL ASSET METRICS")
    print("="*60)
    print(f"{'Asset':<8} {'Weight':<10} {'Return':<12} {'Volatility':<12} {'Sharpe':<10}")
    print("-"*60)
        
    for i, ticker in enumerate(returns.columns):
        r = annualized_return(returns[ticker])
        vol = annualized_volatility(returns[ticker])
        sr = (r - RISK_FREE_RATE) / vol if vol != 0 else 0
        w = f"{weights[i]:.0%}"
        print(f"{ticker:<8} {w:<10} {r:.2%}{'':<2} {vol:.2%}{'':<2} {sr:.2f}")
    print("-"*60)

# =======================
# MAIN EXECUTION
# =======================
if __name__ == "__main__":
    # Download data
    returns = download_data(TICKERS)
    
    # Calculate portfolio metrics
    metrics, portfolio_rets = portfolio_metrics(WEIGHTS, returns, RISK_FREE_RATE)
    
    # Display results
    print("\n" + "="*60)
    print("PORTFOLIO RISK METRICS (HISTORICAL) - 5-ASSET DIVERSIFIED")
    print("="*60)
    for key, value in metrics.items():
        print(f"{key:25} {value}")
    print("="*60)
        
    # Show individual asset metrics
    display_asset_metrics(returns, WEIGHTS)
    
    # Plot cumulative returns
    (1 + portfolio_rets).cumprod().plot(title="Cumulative Returns: 5-Asset Portfolio", figsize=(10, 6))
    plt.ylabel("Growth of $1")
    plt.xlabel("Date")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
