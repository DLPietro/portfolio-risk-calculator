# Portfolio Risk Calculator

📊 A Python tool to calculate **historical risk metrics** for a real-world, diversified n-asset portfolio (n = 5 in this case).

## 🔍 Real-World Case: N-Asset Equally Weighted Portfolio
- **SPY**: S&P 500 ETF (US equities)
- **AGG**: iShares Core U.S. Aggregate Bond ETF (broad bond market)
- **GLD**: SPDR Gold Trust (inflation hedge, low equity correlation)
- **FXE**: CurrencyShares Euro Trust (exposure to EUR/USD)
- **EEM**: iShares MSCI Emerging Markets ETF

All assets weighted at **20%** — a simple, robust, globally diversified strategy.

## 📈 Key Metrics Calculated
- Annualized Return
- Volatility (Standard Deviation)
- Sharpe Ratio (2% risk-free rate)
- Maximum Drawdown
- Historical CVaR (95%)
- Parametric CVaR (95%)

## 📈 Example Output
==================================================
PORTFOLIO RISK METRICS (HISTORICAL)
==================================================
| Annualized Return | 6.82% |

| Volatility | 10.45% |

| Sharpe Ratio (2% Rf) | 0.46 |

| Max Drawdown | -18.32% |

| Historical CVaR (95%) | -1.78% |

| Parametric CVaR (95%) | -1.62% |

==================================================

## 🛠️ Usage
1. Install dependencies:
   ```bash
   pip install yfinance pandas numpy matplotlib
