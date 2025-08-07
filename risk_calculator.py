# risk_calculator.py
# Portfolio Risk Calculator
# Uses models/ and outputs to figures/

# Libraries used for the script: matplotlib, pandas, numpy & yfinance
pip install yfinance pandas numpy matplotlib
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import from models
from models.historical import *                # Model 1: Historical Risk Metrics
from models.parametric import parametric_cvar  # Model 2: Parametric CVaR
from models.ewma import ewma_volatility        # Model 3: EWMA Volatility

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
    data = yf.download(tickers, period=period)["Adj Close"].ffill().dropna()    # Download adjusted closing prices for tickers for a y=5 period
    returns = data.pct_change().dropna()                                        # Forward-fill & drop remaining NaNs
    print(f"Downloaded {len(returns)} days of data")                            # Show daily returns
    return returns                                                              # Calculate daily returns

# =======================
# PORTFOLIO METRICS FUNCTION
# =======================
def portfolio_metrics(weights, returns, rf=0.02):
    """
    Calculate all risk-return metrics for a portfolio
    """
    # Calculate portfolio daily returns
    port_rets = (returns * weights).sum(axis=1)
    
    # Compute metrics
    metrics = {
        "Annualized Return": f"{annualized_return(port_rets):.2%}",
        "Volatility": f"{annualized_volatility(port_rets):.2%}",
        "EWMA Volatility (λ=0.94)": f"{ewma_volatility(port_rets):.2%}",
        "Sharpe Ratio": f"{sharpe_ratio(port_rets, rf):.2f}",
        "Max Drawdown": f"{max_drawdown(port_rets):.2%}",
        "Historical CVaR (95%)": f"{historical_cvar(port_rets, CONFIDENCE_LEVEL):.2%}",
        "Parametric CVaR (95%)": f"{parametric_cvar(port_rets, CONFIDENCE_LEVEL):.2%}"
    }
    return metrics, port_rets

# =======================
# MAIN EXECUTION
# =======================
if __name__ == "__main__":
    # Download data
    returns = download_data(TICKERS)
    
    # Calculate portfolio returns
    metrics, port_rets = portfolio_metrics(WEIGHTS, returns, RISK_FREE_RATE)
    
    # Print results
    print("\n" + "="*60)
    print("PORTFOLIO RISK METRICS (5-ASSET DIVERSIFIED)")
    print("="*60)
    for key, value in metrics.items():
        print(f"{key:25} {value}")
    print("="*60)
    
    # Save results to output/results_summary.md
    with open("output/results_summary.md", "w") as f:
        f.write(f"# Portfolio Risk Analysis Summary\n\n")
        f.write(f"## 📊 5-Asset Equally Weighted Portfolio\n")
        f.write(f"- **SPY**: US Large-Cap Stocks\n")
        f.write(f"- **AGG**: US Aggregate Bonds\n")
        f.write(f"- **GLD**: Gold (Commodity)\n")
        f.write(f"- **FXE**: Euro (Forex)\n")
        f.write(f"- **EEM**: Emerging Markets Equity\n")
        f.write(f"- **Weights**: 20% each\n\n")
        f.write(f"## 📈 Key Metrics (5-Year Historical)\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        for k, v in metrics.items():
            f.write(f"| {k} | {v} |\n")
            
    # Step 5: Plot cumulative returns and save the file
    (1 + port_rets).cumprod().plot(title="Cumulative Returns: 5-Asset Portfolio", figsize=(10, 6))
    plt.ylabel("Growth of $1")
    plt.xlabel("Date")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("output/figures/cumulative_returns.png")
    plt.show()
