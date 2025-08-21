# bootstrap_analysis.py
# PRIVATE SCRIPT: Bootstrapped Historical Simulation
# Do not publish — for internal use only

import pandas as pd
import numpy as np
import yfinance as yf
from models.historical import *
from models.bootstrap import bootstrap_summary

# =======================
# CONFIGURATION
# =======================
TICKERS = ["SPY", "AGG", "GLD", "FXE", "EEM"]
WEIGHTS = [0.2, 0.2, 0.2, 0.2, 0.2]
N_BOOTSTRAP = 5000  # Reduce if needed for speed
RANDOM_STATE = 42

# =======================
# DOWNLOAD DATA
# =======================
def download_data(tickers, period="5y"):
    data = yf.download(tickers, period=period)["Adj Close"].ffill().dropna()
    returns = data.pct_change().dropna()
    portfolio_returns = (returns * WEIGHTS).sum(axis=1)
    print(f"Downloaded {len(returns)} days of data")
    return portfolio_returns

# =======================
# MAIN EXECUTION
# =======================
if __name__ == "__main__":
    print("Running Bootstrapped Historical Simulation...")
    
    # Step 1: Get portfolio returns
    port_rets = download_data(TICKERS)
    
    # Step 2: Run bootstrap
    results = bootstrap_summary(port_rets, n_bootstrap=N_BOOTSTRAP, random_state=RANDOM_STATE)
    
    # Step 3: Print results
    print("\n" + "="*70)
    print("BOOTSTRAPPED HISTORICAL SIMULATION (5,000 SAMPLES)")
    print("="*70)
    for metric, stats in results.items():
        print(f"{metric:20} | Mean: {stats['Mean']:>8} | 95% CI: {stats['95% CI']}")
    print("="*70)
    
    # Optional: Save to CSV (private)
    df = pd.DataFrame(results).T
    df.to_csv("private_bootstrap_results.csv")
    print("\n✅ Results saved to 'private_bootstrap_results.csv'")
