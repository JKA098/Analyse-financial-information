# Real Estate Investment Trust (REIT) Analysis 🏠📊

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Notebook](https://img.shields.io/badge/Notebook-Jupyter-yellow)
![Library](https://img.shields.io/badge/NumPy-enabled-orange)
![Finance](https://img.shields.io/badge/Analysis-REIT%20Returns-lightblue)
![Data](https://img.shields.io/badge/Data-SBRA%20%26%20EQR-lightgrey)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Project Overview
In this project, you'll analyze two publicly traded **Real Estate Investment Trusts (REITs)**:

- **Sabra Health Care REIT Inc. (SBRA)** – Healthcare-focused
- **Equity Residential (EQR)** – Residential apartment-focused

You’ll use **NumPy** and basic financial statistics to assess performance, risk, and return based on their monthly closing stock prices.

---

## 🎓 Learning Objectives
- Analyze stock data with NumPy
- Calculate and compare returns, volatility, and risk metrics
- Practice working in **Jupyter Notebooks** for financial reporting

---

## 🔹 Project Setup

### ✅ Step 1: Local Jupyter Setup
1. Install Python (recommendation: Python 3.9+)
2. Install Jupyter via pip:
```bash
pip install notebook
```
3. Launch Jupyter:
```bash
jupyter notebook
```

### ✅ Step 2: Open the Notebook
- Open `real_estate_investment_trust_analysis_instructions.ipynb`
- Follow each section's instructions step-by-step

---

## 🔢 Key Analysis Tasks

### 📈 Step-by-Step Inside the Notebook

1. **Import Data and NumPy**
   - Load REIT monthly stock prices for SBRA and EQR

2. **Calculate Monthly Log Returns**
   - Use `np.log()` to compute rate of return

3. **Aggregate Annual Returns**
   - Sum of monthly log returns × 12 (if annualizing)

4. **Measure Volatility**
   - Calculate variance and standard deviation of returns

5. **Correlation Between REITs**
   - Use NumPy correlation methods (e.g., `np.corrcoef`)

6. **Interpret the Results**
   - Which REIT has higher return?
   - Which has more risk (volatility)?
   - Are they positively or negatively correlated?

---

## 🌐 Folder Structure
```plaintext
reit_analysis/
├── real_estate_investment_trust_analysis_instructions.ipynb
├── real_estate_investment_trust_analysis_solutions.ipynb
├── prices_sbra.csv
├── prices_eqr.csv
└── README.md
```

---

## 🚀 Optional Enhancements
- Add visualizations with Matplotlib or Seaborn
- Pull live REIT data using the `yfinance` or `pandas_datareader` package
- Write a brief investor summary comparing both REITs

---

## 📄 Example Outputs
```
SBRA Annual Return: 7.8%
EQR Annual Return: 4.3%
SBRA Std Dev: 3.2%
EQR Std Dev: 2.1%
Correlation between SBRA and EQR: 0.47
```

Now you're ready to evaluate REITs like a data-driven investor 🧹!

