# Carly's Clippers: Data Analysis Project 💼💇‍♀️

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Domain](https://img.shields.io/badge/Project-Retail%20Analytics-lightpink)
![Logic](https://img.shields.io/badge/Features-List%20Comprehension%20%26%20Loops-blueviolet)
![Data](https://img.shields.io/badge/Data-Hardcoded%20Lists-lightgrey)
![Learning](https://img.shields.io/badge/Level-Beginner-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)


## 📅 Overview
You're the Data Analyst for Carly’s Clippers, a trendy new hair salon. Carly needs help understanding her sales data to optimize pricing and forecast revenue. In this project, you'll analyze three lists of data representing:

- `hairstyles`: haircut names
- `prices`: corresponding prices for each hairstyle
- `last_week`: how many times each haircut was sold last week

---

## 🔢 Key Objectives
- Calculate average haircut price
- Adjust pricing strategy
- Compute weekly and daily revenue
- Identify cuts priced under $30

---

## 🔹 Step-by-Step Tasks

### 💸 Prices and Cuts

#### ✅ 1. Calculate average haircut price
```python
total_price = 0
for price in prices:
    total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)
```

#### ✅ 2. Reduce all prices by $5
```python
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)
```

---

### 💰 Revenue Calculation

#### ✅ 3. Compute total revenue from last week
```python
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)
```

#### ✅ 4. Calculate average daily revenue
```python
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)
```

---

### 🔶 Cut Filtering

#### ✅ 5. List haircuts under $30
```python
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts Under $30:", cuts_under_30)
```

---

## 🌐 Folder Structure
```plaintext
carly_clippers/
├── README.md
└── analysis.py  # All analysis code goes here
```

---

## 🚀 Extensions
- Add CSV input/output for more dynamic data analysis
- Visualize pricing trends using matplotlib or seaborn
- Build a simple pricing dashboard with Streamlit

---

## 📄 Final Output Examples
```
Average Haircut Price: 31.875
New Prices: [25, 30, 20, 35, 30, 45, 40, 50]
Total Revenue: 1085
Average Daily Revenue: 155.0
Haircuts Under $30: ['bouffant', 'pixie', 'crew cut']
```

Now Carly can make smart decisions based on the insights you've provided!

