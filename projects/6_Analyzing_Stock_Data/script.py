from utils import *

from utils import calculate_variance


def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Write code here

def get_returns(price):
  for n in range(len(price)):
    start_price = price[n]
    end_price = price[n + 1]
    calculate_log_return(start_price, end_price)
  return calculate_log_return()
  return get_returns() 

amazon_returns = get_returns(amazon_prices)

ebay_returns = get_returns(ebay_prices)

print("Amazon returns: ",[display_as_percentage(n) for n in amazon_returns])
print("ebay returns: ",[display_as_percentage(n) for n in ebay_returns])


amazon_anual_returns = sum(amazon_returns)

ebay_anual_returns = sum(ebay_returns)

print("Amazon returns: ", display_as_percentage(amazon_anual_returns))

print("ebay returns: ", display_as_percentage(ebay_anual_returns))

amazon_variance = calculate_variance(amazon_returns)

ebay_variance = calculate_variance(ebay_returns)

print("Amazon returns: ", display_as_percentage(amazon_variance))
print("ebay returns: ", display_as_percentage(ebay_variance))

amazon_stdev = calculate_stddev(amazon_returns)
ebay_stdev = calculate_stddev(ebay_returns)

amazon_correlation = calculate_correlation(amazon_returns)
ebay_correlation = calculate_correlation(ebay_returns)

print("Amazon returns: ", display_as_percentage(amazon_correlation))

print("ebay returns: ", display_as_percentage(ebay_correlation))




