# Project Greenspace: Net Present Value (NPV) Analysis
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Finance](https://img.shields.io/badge/Analysis-NPV-green)
![Learning](https://img.shields.io/badge/Source-Codecademy-8A2BE2)
![Visualization](https://img.shields.io/badge/Plotting-Matplotlib-orange)
![Script](https://img.shields.io/badge/Tool-Python%20Script-yellow)
![Version](https://img.shields.io/badge/version-1.0-green)

## 🌿 Overview
Project Greenspace is a proposed investment initiative aimed at generating long-term revenue after an initial construction phase. The project involves a significant upfront investment followed by years of cash inflows and a final sale. This repository contains a financial model used to evaluate the project's viability using **Net Present Value (NPV)** analysis.


npv_project_greenspace/

├── README.md

├── npv_analysis.py  # Python code to calculate and plot NPV


NPV helps assess the profitability of a project by calculating the present value of projected cash inflows and outflows, discounted at various rates. A positive NPV indicates a potentially profitable investment.

---

## 🎓 Learning Objectives
- Understand the fundamentals of Net Present Value (NPV)
- Analyze how project changes affect profitability
- Learn to model real-life project financing scenarios

---

## ✍️ Project Tasks and Instructions

### ✅ Task 1: Baseline Scenario (Years 1–10)
- **Initial Investment (Year 1):** -$2,000,000
- **Construction Phase:** Years 2–3 (no cash inflows)
- **Revenue Generation:** Years 4–10
  - Revenue from Year 4 onward
  - **Year 10 Final Sale:** $1,000,000
- Objective: Find the discount rate where **NPV = 0**

### ✅ Task 2: Reduced Revenue in Year 4
- **Year 4 Revenue:** Reduce from $250,000 to $50,000
- Rerun the model and observe changes in the NPV curve
- Determine the new breakeven discount rate

### ✅ Task 3: Extended Project Timeline to 15 Years
- Update **Year 10 cash flow** from $1,000,000 to $500,000
- Add **Years 11–14:** $500,000 annually
- **Year 15:** Final sale of $1,000,000

### ✅ Task 4: Update Cash Flow List (`project_a`)
```python
project_a = [
    -2000000, 0, 0, 250000, 300000, 400000, 500000, 600000, 750000,
    500000, 500000, 500000, 500000, 500000, 1000000
]
```



###### from codeacademy