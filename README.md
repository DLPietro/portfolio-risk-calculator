# 🧮 Portfolio Risk Calculator

A Python tool that calculates key financial risk metrics and performs Monte Carlo simulations for diversified portfolios.

## 💡 Features

>Pulls live market data using _yfinance_
>
>Calculates metrics: _Annualized Return, Volatility, Sharpe Ratio, Max Drawdown, CVaR (historical & parametric)_
>
>_Monte Carlo Simulation_ to assess probable portfolio outcomes

---

# 🔍 Portfolio Example: N-Asset Equally Weighted Portfolio
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
