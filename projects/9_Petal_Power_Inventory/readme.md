# Petal Power Inventory Analysis 🌿📊
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Library](https://img.shields.io/badge/Pandas-enabled-orange)
![Project](https://img.shields.io/badge/Analysis-Inventory%20Management-lightblue)
![Data](https://img.shields.io/badge/Data-inventory.csv-yellowgreen)
![Learning](https://img.shields.io/badge/Level-Intermediate-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Project Overview
You’re the lead data analyst for **Petal Power**, a gardening store chain. In this project, you’ll use **Pandas** to analyze store inventory, respond to customer questions, and help marketing create a product catalog using descriptive inventory data.

---

## 🎓 Learning Objectives
- Load and inspect data with Pandas
- Filter DataFrames with conditions
- Create new calculated columns
- Apply lambda functions to rows

---

## 🔹 Step-by-Step Tasks

### ✅ 1. Load the Inventory Data
```python
import pandas as pd

inventory = pd.read_csv("inventory.csv")
```

### ✅ 2. Inspect First 10 Rows
```python
print(inventory.head(10))
```

### ✅ 3. Filter for Staten Island
```python
staten_island = inventory.iloc[:10]
```

### ✅ 4. Get Product Descriptions for Staten Island
```python
product_request = staten_island["product_description"]
```

### ✅ 5. Filter for Brooklyn Seed Products
```python
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
```

---

## 📈 Inventory Calculations

### ✅ 6. Add `in_stock` Column
```python
inventory["in_stock"] = inventory.quantity > 0
```

### ✅ 7. Add `total_value` Column
```python
inventory["total_value"] = inventory.price * inventory.quantity
```

---

## 🌿 Product Descriptions for Marketing

### ✅ 8. Define Combine Lambda Function
```python
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
```

### ✅ 9. Add `full_description` Column
```python
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)
```

---

## 🌐 Folder Structure
```plaintext
petal_power_inventory/
├── README.md
├── script.py          # Analysis logic using pandas
└── inventory.csv      # Inventory data for all store locations
```

---

## 🚀 Extensions
- Visualize product distribution by type and location
- Export `full_description` for use in a marketing CSV
- Add dynamic filtering options for customer service dashboards

---

## 📄 Sample Output Snippets
```
Product Descriptions (Staten Island):
0    daffodil
1    petunia
...

Seed Requests (Brooklyn):
location  product_type  ...
Brooklyn       seeds    ...

Full Descriptions:
potted plant - daffodil
seed - sunflower
```

Petal Power can now confidently serve customers and promote their products 🌺!

