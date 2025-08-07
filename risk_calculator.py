# risk_calculator.py
# Portfolio Risk Calculator
# Uses models/ and outputs to figures/

# Libraries used for the script: matplotlib, pandas, numpy & yfinance
pip install yfinance pandas numpy matplotlib
import yfinance as yf                        # Data from Yahoo Finance
import pandas as pd                          # Data manipulation/analysis
import numpy as np                           # Numerical Operations
import matplotlib.pyplot as plt              # Plots

# Import from models
from models.historical import *                # Model 1: Historical Risk Metrics
from models.parametric import parametric_cvar  # Model 2: Parametric (Gaussian) CVaR
from models.ewma import ewma_volatility        # Model 3: EWMA Volatility
from models.monte_carlo import monte_carlo_simulation  # Model 4: Monte Carlo simulation (GBM)

# =======================
# PORTFOLIO CONFIGURATION AND PARAMETERS
# =======================
TICKERS = ["SPY", "AGG", "GLD", "FXE", "EEM"]  # Sample of 5 different assets
WEIGHTS = [0.2, 0.2, 0.2, 0.2, 0.2]      # Portfolio weights (20% per Asset)
RISK_FREE_RATE = 0.02               # 2% annual risk-free rate
CONFIDENCE_LEVEL = 0.95             # Confidence level CVaR
DAYS_PER_YEAR = 252                 # Trading days in a year

# =======================
# DOWNLOAD DATA
# =======================
def download_data(tickers, period="5y"):
    """Download adjusted closing prices for tickers"""    
    data = yf.download(tickers, period=period)["Adj Close"].ffill().dropna()    # Download adjusted closing prices for tickers for a y=5 period
    returns = data.pct_change().dropna()                                        # Forward-fill & drop remaining NaNs
    print(f"Downloaded {len(returns)} days of data for {tickers}")              # Show daily returns
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
# MONTE CARLO ANALYSIS
# =======================
def analyze_monte_carlo(final_values, alpha=0.95):
    """
    Analyzes the results of Monte Carlo simulation.
    Computes expected/final value, probability of loss, and simulated CVaR.
    """
    mean_final = np.mean(final_values)   # Average final portfolio value
    median_final = np.median(final_values)  # Median final value
    prob_loss = np.mean(final_values < 1000)  # % of paths ending below $1000
    # Simulated CVaR: average of worst 5% outcomes
    cvar = np.mean(final_values[final_values < np.percentile(final_values, 100 * (1 - alpha))])
    
    return {
        "Expected Final Value": f"${mean_final:,.0f}",
        "Median Final Value": f"${median_final:,.0f}",
        "Probability of Loss": f"{prob_loss:.2%}",
        "Simulated CVaR (95%)": f"${cvar:,.0f}"
    }

def plot_monte_carlo_paths(returns, weights, n_paths=100, n_days=252):
    """
    Plots a sample of 100 simulated portfolio paths over 1 year.
    Visualizes potential future outcomes.
    """
    # Portfolio historical return and volatility
    port_rets = (returns * weights).sum(axis=1)
    mu = np.mean(port_rets) * 252  # Annualized return
    sigma = np.std(port_rets) * np.sqrt(252)  # Annualized volatility

    # Time step (daily)
    dt = 1 / 252

    # Initialize simulation matrix
    paths = np.zeros((n_days + 1, n_paths))
    paths[0] = 1000  # Starting value

    # Simulate paths using Geometric Brownian Motion
    for day in range(1, n_days + 1):
        Z = np.random.standard_normal(n_paths)  # Random shock
        paths[day] = paths[day - 1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(paths, color='skyblue', alpha=0.4, linewidth=1)
    plt.title("Monte Carlo Simulation: 100 Sample Paths (1-Year)")
    plt.xlabel("Days")
    plt.ylabel("Portfolio Value ($)")
    plt.axhline(1000, color='red', linestyle='--', label='Initial Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("output/figures/monte_carlo_paths.png")
    plt.show()

# =======================
# MAIN EXECUTION
# =======================
if __name__ == "__main__":
   # Step 1: Download data
    returns = download_data(TICKERS)
    
    # Step 2: Calculate portfolio metrics
    metrics, port_rets = portfolio_metrics(WEIGHTS, returns, RISK_FREE_RATE)
    
    # Step 3: Print basic metrics
    print("\n" + "="*60)
    print("PORTFOLIO RISK METRICS (5-ASSET DIVERSIFIED)")
    print("="*60)
    for key, value in metrics.items():
        print(f"{key:25} {value}")
    
    # Step 4: Run Monte Carlo Simulation
    print("\nRUNNING MONTE CARLO SIMULATION (10,000 paths, 1-year horizon)...")
    final_values = monte_carlo_simulation(
        returns=returns,
        weights=print("="*60)
    
   WEIGHTS,
        n_simulations=10000,
        initial_portfolio=1000
    )

    # Step 5: Analyse & Print Monte Carlo results
    mc_results = analyze_monte_carlo(final_values)
    print("\n" + "="*60)
    print("MONTE CARLO SIMULATION RESULTS")
    print("="*60)
    for key, value in mc_results.items():
        print(f"{key:25} {value}")
    print("="*60)
    
    # Step 6: Save results to output/results_summary.md
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
        f.write(f"\n## 🎲 Monte Carlo Simulation (10,000 paths, 1-year)\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        for k, v in mc_results.items():
            f.write(f"| {k} | {v} |\n")
            
    # Step 7: Plot cumulative returns and save the file
    (1 + port_rets).cumprod().plot(title="Cumulative Returns: 5-Asset Portfolio", figsize=(10, 6))
    plt.ylabel("Growth of $1")
    plt.xlabel("Date")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("output/figures/cumulative_returns.png")
    plt.show()
    
    # Step 8: Plot Monte Carlo paths
    plot_monte_carlo_paths(returns, WEIGHTS)
