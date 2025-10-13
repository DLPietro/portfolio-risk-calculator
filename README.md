# 📃 Portfolio Risk Report

A Python tool that calculates and shows key financial risk metrics and portolio performance using several financial methods, Monte Carlo simulation included.

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

## 🏡 Project Structure

```text
portfolio-risk-calculator/
├── data/
│   └── raw/                # Sample Data
├── models/                 # Calculation Models: Sharpe, CVaR, EWMA, Monte Carlo
│   ├── bootstrp.py
│   ├── ewma.py
│   ├── historical.py
│   ├── monte_carlo.py
│   └── parametric.py
│
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
- [🎲 iGaming Analytics Dashboard](https://github.com/DLPietro/igaming-analytics-case-study) — KPI and players Retention (_Cohort, Church..._)

---

## ⚡ Credits

[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)
[![Email](https://img.shields.io/badge/Email-dileopie-d14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dileopie@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pietro-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pietrodileo)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
