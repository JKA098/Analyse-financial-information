# Sublime Limes' Line Graphs 🌫️📊
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Visualization](https://img.shields.io/badge/Matplotlib-enabled-orange)
![Project](https://img.shields.io/badge/Analysis-Sales%20%26%20Traffic%20Trends-lightblue)
![Output](https://img.shields.io/badge/Export-Graphs%20as%20PNG-yellowgreen)
![Learning](https://img.shields.io/badge/Level-Intermediate-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)
![Library](https://img.shields.io/badge/Matplotlib-enabled-orange)
![Project](https://img.shields.io/badge/Visualization-Line%20Graphs-lightblue)
![Output](https://img.shields.io/badge/Exported-sublime_limes_sales_summary.png-yellowgreen)
![Learning](https://img.shields.io/badge/Level-Beginner-brightgreen)


## 📅 Project Overview
You're working as a data analyst for **Sublime Limes**, an online lime delivery service. The product manager wants to better understand **sales trends** and **page visits** over the past year. You'll use **Matplotlib** to build insightful **line graphs** showing these trends across months.

---

## 🎓 Learning Objectives
- Use Matplotlib to create and customize subplots
- Label axes and legends clearly for insight communication
- Display multiple lines on a single subplot
- Save visualizations to image files

---

## 🔹 Step-by-Step Tasks

### ✅ 1. Setup and Data Review
```python
import codecademylib
import matplotlib.pyplot as plt
```
- Review the provided lists (e.g., `months`, `page_visits`, `key_limes_sold`, etc.)

### ✅ 2. Create Figure and Subplots
```python
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(1, 2, 1)  # Left subplot
ax2 = fig.add_subplot(1, 2, 2)  # Right subplot
```

---

## 🔹 Plotting Page Visits (Left Subplot)
```python
x_values = range(len(months))
ax1.plot(x_values, page_visits, marker='o')
ax1.set_xlabel("Month")
ax1.set_ylabel("Page Visits")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
ax1.set_title("Monthly Page Visits")
```

---

## 🔹 Plotting Lime Sales (Right Subplot)
```python
ax2.plot(x_values, key_limes_sold, color='green', label='Key Limes')
ax2.plot(x_values, persian_limes_sold, color='orange', label='Persian Limes')
ax2.plot(x_values, blood_limes_sold, color='red', label='Blood Limes')
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
ax2.set_title("Monthly Lime Sales by Type")
ax2.legend()
```

---

## 📌 Save Your Work
```python
plt.tight_layout()
plt.savefig("sublime_limes_sales_summary.png")
plt.show()
```

---

## 🌐 Folder Structure
```plaintext
sublime_limes/
├── README.md
├── script.py           # Contains all Matplotlib plotting logic
└── sublime_limes_sales_summary.png  # Output graph image
```

---

## 🚀 Bonus Ideas
- Add gridlines for readability
- Plot a moving average line for trend smoothing
- Export figures for a monthly marketing dashboard

---

## 📄 Sample Output Description
```
Left Plot: Tracks page visits per month with clear x-tick labels
Right Plot: Compares sales of three lime types with distinct colors and a legend
```

You've now built a visual summary of customer activity and sales trends to help Sublime Limes make data-driven decisions! 🍋

