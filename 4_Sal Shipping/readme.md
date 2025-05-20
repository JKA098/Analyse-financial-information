# Sal's Shipping Python Project 🚚
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Topic](https://img.shields.io/badge/Project-Shipping%20Calculator-lightblue)
![Logic](https://img.shields.io/badge/Features-Conditionals%20%26%20Comparison-blueviolet)
![Learning](https://img.shields.io/badge/Level-Beginner-brightgreen)
![Script](https://img.shields.io/badge/Tool-Python%20Script-yellow)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Project Overview
Sal owns the biggest shipping company in the tri-county area and wants to provide customers with the most affordable way to ship their packages. In this project, you'll build a Python program that determines the **cheapest shipping method** based on the package weight.

---

## 💡 Shipping Methods & Prices

### 🚢 Ground Shipping
| Weight Range                     | Price per Pound | Flat Charge |
|----------------------------------|------------------|-------------|
| 2 lb or less                     | $1.50            | $20.00      |
| > 2 lb and ≤ 6 lb              | $3.00            | $20.00      |
| > 6 lb and ≤ 10 lb             | $4.00            | $20.00      |
| > 10 lb                         | $4.75            | $20.00      |

### ✨ Ground Shipping Premium
- Flat Charge: **$125.00** (regardless of weight)

### 🛸 Drone Shipping
| Weight Range                     | Price per Pound | Flat Charge |
|----------------------------------|------------------|-------------|
| 2 lb or less                     | $4.50            | $0.00       |
| > 2 lb and ≤ 6 lb              | $9.00            | $0.00       |
| > 6 lb and ≤ 10 lb             | $12.00           | $0.00       |
| > 10 lb                         | $14.25           | $0.00       |

---

## 🔢 Tasks Breakdown

### 🔹 Step 1: Define the Package Weight
```python
weight = 8.4  # Change as needed for testing
```

### 🔹 Step 2–3: Ground Shipping Logic
```python
# Ground Shipping
if weight <= 2:
    ground_cost = weight * 1.5 + 20
elif weight <= 6:
    ground_cost = weight * 3 + 20
elif weight <= 10:
    ground_cost = weight * 4 + 20
else:
    ground_cost = weight * 4.75 + 20

print("Ground Shipping Cost:", ground_cost)
```

✅ 8.4 lb should yield:
```
8.4 * $4.00 + $20 = $53.60
```

### 🔹 Step 4–5: Premium Ground Shipping
```python
# Ground Shipping Premium
premium_ground_cost = 125.00
print("Premium Ground Shipping Cost:", premium_ground_cost)
```

### 🔹 Step 6–7: Drone Shipping Logic
```python
# Drone Shipping
if weight <= 2:
    drone_cost = weight * 4.5
elif weight <= 6:
    drone_cost = weight * 9.0
elif weight <= 10:
    drone_cost = weight * 12.0
else:
    drone_cost = weight * 14.25

print("Drone Shipping Cost:", drone_cost)
```

✅ 1.5 lb should yield:
```
1.5 * $4.5 = $6.75
```

### 🔹 Step 8: Determine the Cheapest Option
```python
# Determine Cheapest Option
if ground_cost < premium_ground_cost and ground_cost < drone_cost:
    print("Cheapest method is Ground Shipping: $" + str(ground_cost))
elif premium_ground_cost < drone_cost:
    print("Cheapest method is Ground Shipping Premium: $" + str(premium_ground_cost))
else:
    print("Cheapest method is Drone Shipping: $" + str(drone_cost))
```

✅ Results:
- 4.8 lb → Cheapest is **Ground Shipping** ($34.40)
- 41.5 lb → Cheapest is **Ground Shipping Premium** ($125.00)

---

## 🌐 Folder Structure
```plaintext
sal_shipping/
├── README.md

└── shipping.py  # All pricing logic and shipping comparison
```

---

## 🚀 Bonus Ideas
- Accept user input via `input()`
- Turn logic into reusable functions
- Build a simple CLI for real-world usability

