# Getting Ready for Physics Class: Python Fundamentals Project
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Course](https://img.shields.io/badge/Source-Codecademy-8A2BE2)
![Physics](https://img.shields.io/badge/Topic-Physics%20Fundamentals-lightgrey)
![Script](https://img.shields.io/badge/Tool-Python%20Script-yellow)
![Learning](https://img.shields.io/badge/Level-Beginner-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)


## 👩‍🏫 Project Overview
You are a physics teacher preparing materials for the upcoming semester. To help students understand core physics concepts, you decide to create Python functions that calculate temperature conversions, force, energy, and work. This guided project is part of Codecademy's **Python Fundamentals** course.

---

## 📆 Objectives
- Convert between Fahrenheit and Celsius  
- Calculate force, energy, and work  
- Use Python functions with arguments and default parameters

---

## 🔢 Tasks Checklist

### 🔌 Turn Up the Temperature

1. **Fahrenheit to Celsius Function**  
```python
def f_to_c(f_temp):
    return (f_temp - 32) * 5/9
```

2. **Test the function with 100°F**  
```python
f100_in_celsius = f_to_c(100)
```

3. **Celsius to Fahrenheit Function**  
```python
def c_to_f(c_temp):
    return c_temp * 9/5 + 32
```

4. **Test the function with 0°C**  
```python
c0_in_fahrenheit = c_to_f(0)
```

---

### 🚀 Use the Force

5. **Define `get_force(mass, acceleration)`**  
```python
def get_force(mass, acceleration):
    return mass * acceleration
```

6. **Test with train variables**  
```python
train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)
```

7. **Print result**  
```python
print("The GE train supplies", train_force, "Newtons of force.")
```

8. **Define `get_energy(mass, c)` with default `c = 3*10**8`**  
```python
def get_energy(mass, c=3*10**8):
    return mass * c ** 2
```

9. **Test with bomb_mass**  
```python
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
```

10. **Print result**  
```python
print("A 1kg bomb supplies", bomb_energy, "Joules.")
```

---

### 💡 Do the Work

11. **Define `get_work(mass, acceleration, distance)`**  
```python
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
```

12. **Test with train variables**  
```python
train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
```

13. **Print result**  
```python
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
```

---

## 🌐 Folder Structure
```plaintext
getting_ready_physics_class/
├── README.md
├── script.py  # Contains all the function definitions and tests
```

---

## 🚀 Extensions
- Add user input for temperature or mass calculations  
- Wrap in a simple CLI menu for physics learners  
- Visualize work/force with matplotlib

