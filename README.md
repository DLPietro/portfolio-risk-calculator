# 🧮 Portfolio Risk Calculator

A Python tool that calculates key financial risk metrics and performs Monte Carlo simulations for diversified portfolios.

## 💡 Features

>Pulls live market data using _yfinance_
>
>Calculates metrics: _Annualized Return, Volatility, Sharpe Ratio, Max Drawdown, CVaR (historical & parametric)_
>
>Performs _Monte Carlo Simulation_ to assess probable portfolio outcomes over a specified time horizon.

---

## 🚀 Example Usage

To calculate risk metrics for your portfolio, run the following command:

```bash
python risk_calculator.py --assets "SPY,AGG,GLD,FXE,EEM" --start "2020-01-01" --end "2025-01-01"
```

# 🚀 Portfolio Example: N-Asset Equally Weighted Portfolio
- **SPY**: S&P 500 ETF (US equities)
- **AGG**: iShares Core U.S. Aggregate Bond ETF (broad bond market)
- **GLD**: SPDR Gold Trust (inflation hedge, low equity correlation)
- **FXE**: CurrencyShares Euro Trust (exposure to EUR/USD)
- **EEM**: iShares MSCI Emerging Markets ETF

All assets weighted at **20%** — a simple, robust, globally diversified strategy with uncorrelated assets.


## 📊 Example Output

### 📈 Portfolio Risk Metrics (Historical)

| Metric | Value |
|--------|-------|
| Annualized Return | 6.82% |
| Volatility | 10.45% |
| EWMA Volatility (λ=0.94) | 11.12% |
| Sharpe Ratio (2% Rf) | 0.46 |
| Max Drawdown | -18.32% |
| Historical CVaR (95%) | -1.78% |
| Parametric CVaR (95%) | -1.62% |

---

### 💸 Monte Carlo Simulation Results

>Expected Final Value:      $1,068
>
>Median Final Value:        $1,065
>
>Probability of Loss:       28.45%
>
>Simulated CVaR (95%):      $782


## 🛠️ How To Install it
1. Install dependencies:
   ```bash
   pip install yfinance pandas numpy matplotlib
   ```
---

## 🧱 Project Structure

```text
portfolio-risk-calculator/
├── data/
│   └── raw/                # Sample Data
├── models/                 # Calculations: Sharpe, CVaR, Monte Carlo
│   ├── risk_calculations.py
│   ├── monte_carlo.py
├── output/                 # Results: CSV, plots, etc.
├── LICENSE
├── README.md
├── requirements.txt
└── risk_calculator.py
```

---

## 🔗 Related Work

- [📊 My Data Journey Blog](https://dlpietro.github.io) — Weekly updates on my upskilling  
- [🧠 My Learning Roadmap](https://github.com/DLPietro/learning-roadmap) — Publicly tracked progress  
- [📈 Empirical Analysis: S&P 500 vs IVV vs Fidelity](https://github.com/DLPietro/thesis-backtesting-etf-spx) — Using R, GARCH, backtesting  

---

## ⚡ Credits

[![GitHub](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)&nbsp;&nbsp;
[![Commit Style](https://img.shields.io/badge/Commit_Style-DLPietro-9B59B6?style=for-the-badge&logo=git&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/CONTRIBUTING.md)&nbsp;&nbsp;
[![License](https://img.shields.io/badge/License-CC_BY--SA_4.0-007EC7?style=for-the-badge)](https://creativecommons.org/licenses/by-sa/4.0/)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
