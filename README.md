# Portfolio Risk Calculator

📊 A Python tool to calculate **historical risk metrics** for a real-world, diversified 5-asset portfolio.

## 🔍 Real-World Case: 5-Asset Equally Weighted Portfolio
- **SPY**: US Large-Cap Stocks (S&P 500)
- **AGG**: US Aggregate Bonds
- **GLD**: Gold (Commodity)
- **FXE**: Euro (Forex)
- **EEM**: Emerging Markets Equity

All assets weighted at **20%** — a simple, robust, globally diversified strategy.

## 📈 Key Metrics Calculated
- Annualized Return
- Volatility (Standard Deviation)
- Sharpe Ratio (2% risk-free rate)
- Maximum Drawdown
- Historical CVaR (95%)

## 📈 Example Output
==================================================
PORTFOLIO RISK METRICS (HISTORICAL)
==================================================
Annualized Return         6.82%
Volatility                10.45%
Sharpe Ratio              0.46
Max Drawdown              -18.32%
Historical CVaR (95%)     -1.78%
==================================================

## 🛠️ Usage
1. Install dependencies:
   ```bash
   pip install yfinance pandas numpy matplotlib
