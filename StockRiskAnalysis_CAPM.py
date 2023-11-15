import numpy as np
import pandas as pd
import yfinance as yf
from colorama import Fore, Style

# CAPM with monthly Data using logarithmic price change

# Define the risk-free rate
rf = 0.00416  # Blmbrg GTJPY2Y:GOV 14/11/23

# Define tickers
tickers = ["7974.T", "^N225"]

data = pd.DataFrame()

# Fetch monthly adjusted close prices for each ticker
for t in tickers:
    stock_data = yf.download(t, start="2017-1-1", end="2023-12-1", interval="1mo")
    data[t] = stock_data["Adj Close"]
data.iloc[-1,0] = 7014 #Correction of last value of 7974.T registered

# Calculate logarithmic returns and covariance matrix
log_returns = np.log(1 + data.pct_change())
log_returns = log_returns.iloc[1:]
log_returns
cov = log_returns.cov()   # Monthly data, so annualization factor is 12
print("\n")
print(f"La matriz de covarianzas de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} con el {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es")
print(cov)


# Calculate compounded return for the market
total_compounded_return_market = (1 + log_returns[tickers[1]]).prod() - 1

# Calculate monthly return for the market
monthly_return_market = (1 + total_compounded_return_market) ** (1 / (len(log_returns))) - 1

# Annualize monthly return
annualized_return_market = (1 + monthly_return_market) ** 12 - 1

# Covariance with the market
cov_market = cov.iloc[0, 1]
market_var = cov.iloc[1, 1]  
stock_beta = cov_market / market_var

print("\n")
print(f"La {Style.BRIGHT}Tasa libre de riesgo{Style.RESET_ALL} usando el GTJPY5Y es: {round(rf * 100, 4)}%")
print("\n")
print(f"El {Fore.YELLOW}{Style.BRIGHT}Retorno de Mercado{Style.RESET_ALL} del {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(total_compounded_return_market * 100, 4)}%")

# Covariance
print(f"La {Fore.GREEN}{Style.BRIGHT}Covarianza{Style.RESET_ALL} de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} con el {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(cov_market * 100, 4)}%")
print(f"La {Fore.GREEN}{Style.BRIGHT}Varianza{Style.RESET_ALL} del {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(market_var * 100, 4)}%")

# Beta
print(f"La {Fore.RED}{Style.BRIGHT}Beta{Style.RESET_ALL} de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} con el {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(stock_beta, 5)}")

# Calculation of CAPM
riskpremium = (annualized_return_market - rf)
stock_capm_return = rf + stock_beta * riskpremium
sharpe = (stock_capm_return - rf) / (log_returns[tickers[0]].std() * 12 ** 0.5)
print('\n')
print(f"El {Style.BRIGHT}Re{Style.RESET_ALL} por CAPM de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} es de: {Style.BRIGHT}{Fore.BLUE}{round(stock_capm_return * 100, 3)}%{Style.RESET_ALL}")
print(f'El {Style.BRIGHT}Ratio de Sharpe {Style.RESET_ALL}de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} es de: {Style.BRIGHT}{Fore.BLUE}{round(sharpe, 3)}')


# CAPM with monthly Data using porcentual price change

import numpy as np
import pandas as pd
import yfinance as yf
from colorama import Fore, Style

# Define the risk-free rate
rf = 0.00416  # Blmbrg GTJPY2Y:GOV 14/11/23

# Define tickers
tickers = ["7974.T", "^N225"]

data = pd.DataFrame()

# Fetch monthly adjusted close prices for each ticker
for t in tickers:
    stock_data = yf.download(t, start="2017-1-1", end="2023-12-1", interval="1mo")
    data[t] = stock_data["Adj Close"]
data.iloc[-1,0] = 7014 #Correction of last value of 7974.T registered

# Calculate logarithmic returns and covariance matrix
returns = data.pct_change()
returns = returns.iloc[1:]
returns
cov = returns.cov()   # Monthly data, so annualization factor is 12
print("\n")
print(f"La matriz de covarianzas de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} con el {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es")
print(cov)


# Calculate compounded return for the market
total_compounded_return_market = (1 + returns[tickers[1]]).prod() - 1

# Calculate monthly return for the market
monthly_return_market = (1 + total_compounded_return_market) ** (1 / (len(returns))) - 1

# Annualize monthly return
annualized_return_market = (1 + monthly_return_market) ** 12 - 1

# Covariance with the market
cov_market = cov.iloc[0, 1]
market_var = cov.iloc[1, 1]  
stock_beta = cov_market / market_var

print("\n")
print(f"La {Style.BRIGHT}Tasa libre de riesgo{Style.RESET_ALL} usando el GTJPY5Y es: {round(rf * 100, 4)}%")
print("\n")
print(f"El {Fore.YELLOW}{Style.BRIGHT}Retorno de Mercado{Style.RESET_ALL} del {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(total_compounded_return_market * 100, 4)}%")

# Covariance
print(f"La {Fore.GREEN}{Style.BRIGHT}Covarianza{Style.RESET_ALL} de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} con el {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(cov_market * 100, 4)}%")
print(f"La {Fore.GREEN}{Style.BRIGHT}Varianza{Style.RESET_ALL} del {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(market_var * 100, 4)}%")

# Beta
print(f"La {Fore.RED}{Style.BRIGHT}Beta{Style.RESET_ALL} de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} con el {Style.BRIGHT}{tickers[1]}{Style.RESET_ALL} es {round(stock_beta, 5)}")

# Calculation of CAPM
riskpremium = (annualized_return_market - rf)
stock_capm_return = rf + stock_beta * riskpremium
sharpe = (stock_capm_return - rf) / (returns[tickers[0]].std() * 12 ** 0.5)
print('\n')
print(f"El {Style.BRIGHT}Re{Style.RESET_ALL} por CAPM de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} es de: {Style.BRIGHT}{Fore.BLUE}{round(stock_capm_return * 100, 3)}%{Style.RESET_ALL}")
print(f'El {Style.BRIGHT}Ratio de Sharpe {Style.RESET_ALL}de {Style.BRIGHT}{tickers[0]}{Style.RESET_ALL} es de: {Style.BRIGHT}{Fore.BLUE}{round(sharpe, 3)}')
