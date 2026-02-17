import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize

# 1. Données
tickers = ['SPUS', 'ISDE.L', 'FNV', 'BHP', 'NEE']
data = yf.download(tickers, start='2020-01-01', end='2025-10-10')['Close']
returns = data.pct_change().dropna()

# 2. Statistiques
mean_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

# 3. Fonctions
def portfolio_performance(weights, mean_returns, cov_matrix):
    ret = np.dot(weights,mean_returns)
    vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return ret, vol

def negative_sharpe(weights, mean_returns, cov_matrix):
    ret, vol = portfolio_performance(weights, mean_returns, cov_matrix)
    return -ret / vol

# 4. Optimisation
n = len(tickers)
constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1},{'type':'ineq','fun': lambda w: 0.125 - np.sqrt(np.dot(w.T, np.dot(cov_matrix, w)))}]

bounds = tuple((0, 1) for _ in range(n))
initial = np.array([1/n] * n)

result = minimize(negative_sharpe, initial, args=(mean_returns, cov_matrix),
                  method='SLSQP', bounds=bounds, constraints=constraints)

# 5. Résultats
optimal_weights = result.x
opt_ret, opt_vol = portfolio_performance(optimal_weights, mean_returns, cov_matrix)

print("Poids optimaux:")
for ticker, weight in zip(tickers, optimal_weights):
    print(f"{ticker}: {weight:.2%}")
print(f"\nRendement: {opt_ret:.2%}")
print(f"Volatilité: {opt_vol:.2%}")
print(f"Sharpe: {opt_ret/opt_vol:.3f}")

