# Betty's Bakery 🍪 Inventory Planning with NumPy

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Library](https://img.shields.io/badge/NumPy-enabled-orange)
![Topic](https://img.shields.io/badge/Project-Inventory%20Planning-lightblue)
![Data](https://img.shields.io/badge/Data-recipes.csv-yellowgreen)
![Learning](https://img.shields.io/badge/Level-Beginner-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)

## 📅 Overview
Betty is preparing to launch her bakery and wants to estimate how much of each ingredient she needs to buy. You'll help her use **NumPy arrays** to analyze recipes and calculate bulk ingredient needs for baking cupcakes, cookies, and more.

---

## 📚 Learning Objectives
- Practice array creation and manipulation with NumPy
- Use indexing, slicing, and logical comparisons
- Perform element-wise operations to calculate bulk quantities

---

## 🔹 Step-by-Step Tasks

### ✅ 1. Import NumPy
```python
import numpy as np
```

### ✅ 2. Create Array for Cupcake Recipe
```python
# Format: [Flour, Sugar, Eggs, Milk, Butter]
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
```

### ✅ 3. Load All Recipes from CSV
```python
recipes = np.genfromtxt("recipes.csv", delimiter=",")
```

### ✅ 4. Display All Recipes
```python
print(recipes)
```

### ✅ 5. Select the 3rd Column (Eggs)
```python
eggs = recipes[:, 2]  # 0-indexed column 3
```

### ✅ 6. Find Recipes with Exactly 1 Egg
```python
one_egg_recipes = eggs == 1
print(one_egg_recipes)
```

### ✅ 7. Create Array for Cookies (3rd row)
```python
cookies = recipes[2, :]  # 3rd row (index 2)
```

### ✅ 8. Double Batch of Cupcakes
```python
double_batch = cupcakes * 2
```

### ✅ 9. Create Final Grocery List
```python
grocery_list = double_batch + cookies
print("Grocery List:", grocery_list)
```

---

## 🌐 Folder Structure
```plaintext
betty_bakery/
├── README.md
├── bakery.py       # All recipe and grocery list logic
└── recipes.csv     # Ingredients data for each recipe
```

---

## 🚀 Bonus Challenges
- Add a pie chart or bar graph to visualize ingredient demand
- Expand the CSV to include more baked goods
- Build a GUI to select recipes and generate shopping lists

---

## 🍔 Sample Output
```
[2.  0.75 2.  1.  0.5 ]  # Cupcakes
[[...], [...], [...], [...]]  # Recipes
[False  True False False]  # Recipes using 1 egg
Grocery List: [7.  3.25 5.  3.  2. ]
```

Now Betty knows exactly what to order for opening day!

