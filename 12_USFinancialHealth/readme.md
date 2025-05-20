# US Financial Health Analysis 🌎📊
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Data](https://img.shields.io/badge/Data-FRED%20%26%20World%20Bank-lightgrey)
![Library](https://img.shields.io/badge/Pandas%20%26%20NumPy-enabled-orange)
![Finance](https://img.shields.io/badge/Analysis-Macro%20%26%20Market%20Volatility-lightblue)
![Learning](https://img.shields.io/badge/Level-Advanced-red)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Project Overview
In this project, you’ll explore the financial health of the **United States from 1999 to 2019**. By importing and analyzing **stock market data, commodity prices, GDP, and export values**, you’ll calculate **log returns** to assess volatility and economic stability.

---

## 🎓 Learning Objectives
- Import and clean financial data from CSV and APIs (FRED, World Bank)
- Calculate log returns of price data using NumPy
- Measure volatility through statistical metrics like variance
- Compare trends in commodities, stock indices, and macroeconomic indicators

---

## 🔹 Tasks & Steps

### 📈 Importing Commodity Prices
```python
import pandas as pd
gold_prices = pd.read_csv("gold_prices.csv")
crude_oil_prices = pd.read_csv("crude_oil_prices.csv")
print(gold_prices.head())
print(crude_oil_prices.head())
```

### 📈 Importing Stock Market Data (FRED API)
```python
import pandas_datareader.data as web
import datetime

start = datetime.datetime(1999, 1, 1)
end = datetime.datetime(2019, 1, 1)

nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)
sap_data = web.DataReader("SP500", "fred", start, end)
```

### 📈 Importing World Bank Data
```python
import pandas_datareader.wb as wb

gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)
```

---

## 🔢 Calculating Log Returns
```python
import numpy as np

def log_return(prices):
    return np.log(prices / prices.shift(1))

# Apply to each dataset
gold_returns = log_return(gold_prices['Gold_Price'])
crudeoil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data["NASDAQ100"])
sap_returns = log_return(sap_data["SP500"])
gdp_returns = log_return(gdp_data["NY.GDP.MKTP.CD"])
export_returns = log_return(export_data["NE.EXP.GNFS.CN"])
```

---

## 📊 Analyzing Volatility with Variance
```python
print("Gold Volatility:", gold_returns.var())
print("Oil Volatility:", crudeoil_returns.var())
print("NASDAQ Volatility:", nasdaq_returns.var())
print("S&P 500 Volatility:", sap_returns.var())
print("GDP Volatility:", gdp_returns.var())
print("Export Volatility:", export_returns.var())
```

Interpret these values to compare which assets were most and least volatile across the 20-year period.

---

## 🌐 Folder Structure
```plaintext
us_financial_health/
├── README.md

├── gold_prices.csv

├── crude_oil_prices.csv

├── analysis.py           # Log return and volatility logic
```

---

## 🚀 Extension Ideas
- Plot time series and log returns using Matplotlib or Seaborn
- Create correlation heatmaps across all return series
- Perform rolling variance and volatility clustering

---

## 📄 Example Output
```
Gold Volatility: 0.0142
Oil Volatility: 0.0279
NASDAQ Volatility: 0.0311
S&P 500 Volatility: 0.0257
GDP Volatility: 0.0061
Exports Volatility: 0.0083
```

This analysis empowers you to assess financial risk across sectors and periods of macroeconomic change. 👌

