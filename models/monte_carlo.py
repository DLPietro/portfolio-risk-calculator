# models/monte_carlo.py
# Monte Carlo Simulation for Portfolio Risk (Geometric Brownian Motion)
# Simulates future portfolio paths and calculates risk metrics

import numpy as np
import pandas as pd

def monte_carlo_simulation(returns, weights, n_simulations=1000, n_days=252, initial_portfolio=1000):
    """
    Run Monte Carlo simulation for portfolio returns
    :param returns: DataFrame of daily returns
    :param weights: List of portfolio weights
    :param n_simulations: Number of paths to simulate
    :param n_days: Time horizon (1 year = 252 days)
    :param initial_portfolio: Starting portfolio value
    :return: Array of final portfolio values
    """
    # Portfolio historical return and volatility
    port_returns = (returns * weights).sum(axis=1)
    mu = np.mean(port_returns) * 252  # Annualized return
    sigma = np.std(port_returns) * np.sqrt(252)  # Annualized volatility

    # Generate random returns using GBM
    dt = 1 / 252  # Daily time step
    simulations = np.zeros((n_days, n_simulations))
    simulations[0] = initial_portfolio

    for day in range(1, n_days):
        # Random shock
        Z = np.random.standard_normal(n_simulations)
        # GBM formula
        simulations[day] = simulations[day - 1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    # Return final values
    return simulations[-1, :]
