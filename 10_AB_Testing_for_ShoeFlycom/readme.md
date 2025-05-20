# A/B Testing for ShoeFly.com 📲🩾
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Library](https://img.shields.io/badge/Pandas-enabled-orange)
![Project](https://img.shields.io/badge/Analysis-A%2FB%20Testing-lightblue)
![Data](https://img.shields.io/badge/Data-ad_clicks.csv-yellowgreen)
![Learning](https://img.shields.io/badge/Level-Intermediate-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Project Overview
ShoeFly.com is running an A/B test to determine which of two ads performs better. These ads appear on different platforms (Facebook, Google, Twitter, Email) across the week. You'll help the team evaluate ad performance using **Pandas** and **grouped aggregations**.

---

## 🎓 Learning Objectives
- Use grouping and pivoting in Pandas
- Analyze ad click data by source, day, and experimental group
- Calculate click-through rates
- Evaluate A/B test effectiveness

---

## 🔹 Step-by-Step Tasks

### ✅ 1. Load & Inspect the Data
```python
import pandas as pd
ad_clicks = pd.read_csv("ad_clicks.csv")
print(ad_clicks.head())
```

### ✅ 2. Count Views by Platform
```python
print(ad_clicks.groupby("utm_source").user_id.count().reset_index())
```

### ✅ 3. Create is_click Column
```python
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
```

### ✅ 4. Group by Source and Click Status
```python
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
```

### ✅ 5. Pivot to Compare Clicks
```python
clicks_pivot = clicks_by_source.pivot(
    columns="is_click",
    index="utm_source",
    values="user_id"
)
```

### ✅ 6. Calculate Percent Clicked
```python
clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)
```

---

## 🔍 Analyzing the A/B Test

### ✅ 7. Compare Groups A and B
```python
print(ad_clicks.groupby("experimental_group").user_id.count().reset_index())
```

### ✅ 8. Click-Through Rate by Group
```python
print(ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index())
```

### ✅ 9. Filter Group A and Group B
```python
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
```

### ✅ 10. Percent Clicked Per Day
```python
a_by_day = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()
a_pivot = a_by_day.pivot(columns="is_click", index="day", values="user_id")
a_pivot["percent_clicked"] = a_pivot[True] / (a_pivot[True] + a_pivot[False])

b_by_day = b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()
b_pivot = b_by_day.pivot(columns="is_click", index="day", values="user_id")
b_pivot["percent_clicked"] = b_pivot[True] / (b_pivot[True] + b_pivot[False])
```

### ✅ 11. Compare A vs. B
- Compare `a_pivot` vs `b_pivot`
- Determine if there's a day when one ad clearly outperformed the other

---

## 🌐 Folder Structure
```plaintext
shoefly_ab_test/
├── README.md
├── ad_clicks.csv       # Dataset for analysis
└── analysis.py         # Code for grouping, pivoting, and CTR comparison
```

---

## 🚀 Extension Ideas
- Visualize CTRs with bar charts using matplotlib/seaborn
- Add heatmaps to spot patterns across days and platforms
- Build a summary dashboard in Streamlit or Jupyter

---

## 📄 Example Output
```
utm_source    True    False   percent_clicked
Facebook      124     376     0.248
Google        210     490     0.300
...

Ad A performed better on Mon-Wed
Ad B had higher CTR Thu-Sat
Recommendation: A for weekdays, B for weekends
```

Now you can recommend a smarter, data-backed ad strategy for ShoeFly.com!