import codecademylib3_seaborn
import codecademylib3_seaborn
import pandas as pd # for data manipulation
import pandas_datareader.data as web # for loading nasdaq and sp500 data

from datetime import datetime as dt # for time manipulation
import pandas_datareader.wb as wb # for loading gdp data
import numpy as np # for log return calculation


#import gold and crude oil prices
gold_prices = pd.read_csv('gold_prices.csv', header = 0)
crude_oil_prices = pd.read_csv('crude_oil_prices.csv', header = 0)
print(gold_prices)
print(crude_oil_prices)

# define the start and end periods
start = dt(1999 ,1,1)
end = dt(2019 ,1,1)

# load nasdaq and sp500 data
nasdaq_data = web.DataReader('NASDAQ100','fred', start, end)
print(nasdaq_data)

sap_data = web.DataReader('SP500','fred',start, end)
print(sap_data)


# load GDP data
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
#print(gdp_data)

# load value of goods and services
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)
print(export_data)

# Calculating Log Return
def log_return (prices):
    return np.log(prices/prices.shift(1))

# Calculating Log Return for gold_prices
gold_returns = log_return(gold_prices['Gold_Price'])
print(gold_returns)

# Calculating Log Return for crude_oil_prices
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
print(crude_oil_returns)

# Calculating Log Return for nasdaq_data
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
#print(nasdaq_returns)

# Calculating Log Return for sap_data
sap_returns = log_return(sap_data['SP500'])
#print(sap_returns)

gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])

export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

print(f"The variance for gold is: {gold_returns.var()}")
print(f"The variance for crude_oil_returns is: {crude_oil_returns.var()}")
print(f"The variance for nasdaq_returns is: {nasdaq_returns.var()}")
print(f"The variance for sap_returns is: {sap_returns.var()}")
print(f"The variance for gdp_returns is: {gdp_returns.var()}")
print(f"The variance for export_returns is: {export_returns.var()}")



