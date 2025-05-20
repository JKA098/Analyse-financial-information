# Analyzing Stock Data 📈 Python Project

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Finance](https://img.shields.io/badge/Analysis-Stock%20Returns-green)
![Math](https://img.shields.io/badge/Features-Log%20Returns%20%26%20Correlation-blueviolet)
![Tools](https://img.shields.io/badge/Helper%20Module-utils.py-yellow)
![Learning](https://img.shields.io/badge/Level-Intermediate-orange)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Overview
You're analyzing the monthly stock prices of **Amazon (AMZN)** and **eBay (EBAY)** from June 2018 to June 2019. This project involves calculating **logarithmic returns**, **annual return**, and assessing **investment risk** through **variance**, **standard deviation**, and **correlation**.

---

## 🎓 Learning Goals
- Calculate logarithmic rates of return
- Analyze risk using variance and standard deviation
- Assess correlation between two stocks
- Present financial results as formatted percentages

---

## 🔢 Data & Tools
- Monthly stock price data for AMZN and EBAY
- `utils.py` helper functions:
  - `calculate_log_return(start_price, end_price)`
  - `calculate_variance(data)`
  - `calculate_stddev(data)`
  - `calculate_correlation(x, y)`
  - `display_as_percentage(value)`

---

## 🔹 Step-by-Step Tasks

### ✅ 1. Inspect the Data
- Familiarize yourself with `script.py` (main analysis logic)
- Review `utils.py` for reusable financial functions

### ✅ 2. Define `get_returns()`
```python
def get_returns(prices):
    returns = []
    for i in range(len(prices) - 1):
        start = prices[i]
        end = prices[i + 1]
        returns.append(calculate_log_return(start, end))
    return returns
```

### ✅ 3. Generate Return Lists
```python
amazon_returns = get_returns(amzn)
ebay_returns = get_returns(ebay)
```

### ✅ 4. Display Monthly Returns as Percentages
```python
print([display_as_percentage(r) for r in amazon_returns])
print([display_as_percentage(r) for r in ebay_returns])
```

### ✅ 5. Calculate Annual Return
```python
annual_amzn = sum(amazon_returns)
annual_ebay = sum(ebay_returns)
print("Amazon Annual Return:", display_as_percentage(annual_amzn))
print("eBay Annual Return:", display_as_percentage(annual_ebay))
```

### ✅ 6. Calculate Variance (Risk)
```python
amzn_var = calculate_variance(amazon_returns)
ebay_var = calculate_variance(ebay_returns)
print("Amazon Variance:", amzn_var)
print("eBay Variance:", ebay_var)
```

### ✅ 7. Standard Deviation
```python
amzn_std = calculate_stddev(amazon_returns)
ebay_std = calculate_stddev(ebay_returns)
print("Amazon Std Dev:", display_as_percentage(amzn_std))
print("eBay Std Dev:", display_as_percentage(ebay_std))
```

### ✅ 8. Correlation Between Stocks
```python
correlation = calculate_correlation(amazon_returns, ebay_returns)
print("Amazon/eBay Correlation:", correlation)
```

---

## 🌐 Folder Structure
```plaintext
analyzing_stock_data/
├── README.md
├── script.py           # Analysis logic
├── utils.py            # Helper financial/statistical functions
└── data.csv (optional) # If external data loading is added
```

---

## 🚀 Bonus Ideas
- Visualize returns with matplotlib
- Add a CSV parser to load external stock data
- Build a web dashboard using Streamlit

---

## 📄 Example Output Snippets
```
Amazon Annual Return: 10.8%
eBay Annual Return: 3.4%
Amazon Std Dev: 4.5%
eBay Std Dev: 2.9%
Amazon/eBay Correlation: 0.64
```

You're now ready to compare these two investments and advise on risk and reward!

