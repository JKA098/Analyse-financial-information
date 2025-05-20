# Magic 8-Ball 🧙‍♂️ Python Project
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/made%20with-Python-3776AB)
![Project](https://img.shields.io/badge/type-Fun%20Mini%20App-purple)
![Module](https://img.shields.io/badge/Library-random-lightgrey)
![Logic](https://img.shields.io/badge/Features-Conditionals%20%26%20Input-blueviolet)
![Learning](https://img.shields.io/badge/Level-Beginner-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-green)

## 🌟 Overview
The **Magic 8-Ball** is a fun fortune-telling toy that answers yes/no questions. In this project, you'll build your own Magic 8-Ball simulator using Python. Each time the script runs, it will provide a different answer randomly selected from a list of fortunes.

---

## 🎓 Learning Objectives
- Use the `random` module
- Write conditional logic using `if`, `elif`, and `else`
- Handle user input and edge cases with `if` statements

---

## 🔢 Core Tasks Breakdown

### ⚖️ Setup
```python
# 1. Set up the name and question variables
name = "Joe"
question = "Is this real life?"
answer = ""  # To be set later
```

### 💡 Generate Random Response
```python
# 2. Import the random module and generate a number
import random
random_number = random.randint(1, 9)  # Random number from 1 to 9
```

### ⏬ Decision Making with if/elif/else
```python
# 3. Assign answer based on random_number
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"
```

### 📈 Output the Result
```python
# 4. Handle formatting
if question == "":
    print("You need to ask a question!")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
```

---

## 🪩 Example Output
```
Joe asks: Is this real life?
Magic 8-Ball's answer: Better not tell you now
```

---

## 🌐 Folder Structure
```plaintext
magic_8_ball/
├── README.md

└── magic8.py  # Contains all the logic and random response generation
```



## 🎯 Goal
Build a dynamic, fun Magic 8-Ball Python script that handles randomness, input variations, and outputs clean, user-friendly messages.

Run your program several times to see the magic in action!

