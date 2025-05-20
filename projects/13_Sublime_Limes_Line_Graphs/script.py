import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here

plt.figure(figsize=(12,8)) # task 1
plt.plot(visits_per_month, key_limes_per_month) 


ax1 = plt.subplot(1, 2, 1) # task 2
x_values = range(len(months)) # task 4
ax1.plot(x_values,visits_per_month, marker="o") # task 5
ax1.set_xlabel("Number of months") # task 6
ax1.set_ylabel("Number of visits") # task 6
ax1.set_title("Number of Visits per Month") # task 6
ax1.set_xticks(x_values) # task 7
ax1.set_xticklabels(months) # task 8

ax2 = plt.subplot(1, 2, 2) # task 3

# task 9
ax2.plot(x_values, key_limes_per_month, label="Key Limes", marker="o")
ax2.plot(x_values, persian_limes_per_month, label="Persian Limes", marker="s")
ax2.plot(x_values, blood_limes_per_month, label="Blood Limes", marker="^")


ax2.legend() # task 10
ax2.set_xticks(x_values) # task 10
ax2.set_xticklabels(months) # task 10
ax2.set_title("Distribution of limes") # task 11

plt.savefig('Sublime_graphs.png') # task 12

plt.tight_layout()
plt.show()
