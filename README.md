# Optimization-Financial-Modelling

## Overview

This repository contains Python scripts for estimating the expected return of a given stock using the Capital Asset Pricing Model (CAPM) with Fama-French three-factor data and linear regression. The analysis focuses on understanding the relationship between the stock's returns and market factors to make informed predictions about its future performance.

## Contents

- **StockRiskAnalysis_CAPM.py** Python script automating the download of monthly stock prices, calculating returns, obtaining Fama-French factors, and estimating the expected return using CAPM.

- **CAPM_OLS_Regression.py:** Module for retrieving Fama-French three-factor model data and using regular OLS regression for CAPM Beta estimation.

## How to Use

1. Ensure you have the necessary Python libraries installed. You can install them using:

   ```bash
   pip install pandas yfinance statsmodels matplotlib seaborn colorama
Disclaimer
This analysis is for educational and informational purposes only. The estimated expected return is based on historical data and assumptions. It is not financial advice, and users should conduct thorough research and consider professional advice before making investment decisions.

Author
Miguel Ángel Martínez
