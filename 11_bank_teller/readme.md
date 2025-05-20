# Bank Teller Queue Simulation 🏦🤝
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Simulation](https://img.shields.io/badge/Project-Queue%20Simulation-lightblue)
![Library](https://img.shields.io/badge/NumPy-enabled-orange)
![Visualization](https://img.shields.io/badge/Matplotlib-optional-yellow)
![Learning](https://img.shields.io/badge/Level-Intermediate-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Project Overview
This project simulates a **bank teller queue system** to analyze how customers wait in line, how long they are served, and how different teller availability affects wait times. It’s designed to build your skills in simulating queue-based systems using **Python**, **NumPy**, and optionally **Matplotlib** for visualization.

---

## 🎓 Learning Objectives
- Understand queue dynamics and discrete event simulation
- Apply Python for real-world modeling problems
- Use NumPy for generating random service and arrival times
- Analyze and visualize wait time distributions

---

## 🔹 Task Overview

### ✅ 1. Setup and Imports
- Import `numpy`, `random`, `matplotlib.pyplot`, and define global constants (e.g., average arrival rate, service time)

### ✅ 2. Simulate Customer Arrivals
- Generate a list of arrival times using an exponential distribution
```python
arrival_times = np.cumsum(np.random.exponential(scale=mean_interarrival_time, size=NUM_CUSTOMERS))
```

### ✅ 3. Simulate Teller Availability
- Initialize teller availability times and assign customers to the first available teller

### ✅ 4. Track Wait Times and Service Durations
- For each customer:
  - Determine wait time (if any)
  - Calculate service start and end times

### ✅ 5. Store Results in Lists
- Append each customer's wait time, teller ID, and total time in system to a results list or DataFrame

### ✅ 6. Analyze Statistics
- Compute average wait time, max wait time, service time, etc.
- Print a report of key metrics

### ✅ 7. Optional: Visualize Results
- Plot histogram of wait times
- Plot number of customers in queue over time

---

## 🌐 Folder Structure
```plaintext
bank_teller_simulation/
├── README.md
├── bank_teller_instructions.ipynb  # Instructions for simulation tasks
├── bank_teller_solution.ipynb      # (Optional) Reference solution
└── teller_sim.py                   # Python simulation script (if converted)
```

---

## 🚀 Extensions & Challenges
- Simulate multiple bank branches with different numbers of tellers
- Introduce customer priority queues
- Run Monte Carlo simulations to estimate optimal teller count

---

## 📊 Sample Metrics Output
```
Average Wait Time: 4.7 minutes
Maximum Wait Time: 13.5 minutes
Average Time in System: 10.2 minutes
```

You're now ready to simulate real-world queue dynamics in a bank and recommend staffing strategies! 🛋️

