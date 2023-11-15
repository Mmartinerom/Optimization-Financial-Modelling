import pandas as pd
import yfinance as yf
import datetime as dt
import statsmodels.api as sm
import matplotlib.pyplot as plt
import getFamaFrenchFactors as gff
import seaborn as sns
from colorama import Fore, Style

#Parameters
end =  dt.date(2023,11,1)
start = dt.date(2016,12,31)
ticker = ['7974.T'] 

#Automatizing Data download
stock_prices = yf.download(ticker, start, end)['Adj Close']
stock_prices

#Convert data to monthly prices
stock_prices = stock_prices.resample("1M").last()
stock_prices.head()

#Monthly returns
stock_returns = stock_prices.pct_change()
stock_returns = pd.DataFrame(stock_returns.dropna())


#Market Excess Returns

ff3_monthly = pd.DataFrame(gff.famaFrench3Factor(frequency = "m"))
ff3_monthly.rename(columns = {"date_ff_factors": "Date"}, inplace = True)
ff3_monthly.set_index("Date", inplace = True)

#Merging the FF & the Change in Price for 7974
data = ff3_monthly.merge(stock_returns,on = "Date")
#Excess return 7974.T
data.rename(columns = {"Adj Close": "7974.T"}, inplace = True)
excess_ret = data["7974.T"] - data["RF"]
data["7974.T-RF"] = excess_ret
data

#Checking the relationships between the two variables
sns.regplot(x = "Mkt-RF", y ="7974.T-RF", data = data)

#OLS regression
x = data["Mkt-RF"]
y = data["7974.T-RF"]

x1 = sm.add_constant(x) #constant
model = sm.OLS(y,x1)

results = model.fit()
results.summary()

#Saving parameters
intercept, beta = results.params
beta

#Expected Return Calculation using Betas

# rf rate
rf = 0.00416  # Blmbrg GTJPY2Y:GOV 14/11/23
mktprem = data["Mkt-RF"].mean()
Nintendo_exp_ret = (rf + beta*mktprem)*12*100
print(f"El {Style.BRIGHT}Re{Style.RESET_ALL} por CAPM de {Style.BRIGHT}{ticker[0]}{Style.RESET_ALL} es de: {Style.BRIGHT}{Fore.BLUE}{round(Nintendo_exp_ret, 3)}%{Style.RESET_ALL}")
