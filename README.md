# Portfolio Risk Calculator

📊 A Python tool to calculate **historical risk metrics** for financial portfolios, inspired by my Master's thesis on S&P 500, IVV, and Fidelity Contrafund.

## 🔍 Features
- Downloads real ETF data using `yfinance`
- Calculates key risk/return metrics:
  - Annualized Return
  - Volatility
  - Sharpe Ratio
  - Maximum Drawdown
  - Historical CVaR (95%)
- Fully replicable and open-source

## 📈 Example Output
==================================================
PORTFOLIO RISK METRICS (HISTORICAL)
==================================================
Annualized Return         10.80%
Volatility                13.50%
Sharpe Ratio              0.65
Max Drawdown              -34.20%
Historical CVaR (95%)     -2.10%
==================================================

## 🛠️ Usage
1. Install dependencies:
   ```bash
   pip install yfinance pandas numpy matplotlib
