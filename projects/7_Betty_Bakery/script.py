# task1
import numpy as np

# task2
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
# print(cupcakes)

# task3
recipes = np.genfromtxt( "recipes.csv", delimiter=',')

# task4
print(recipes)

# task5
eggs = recipes [:,2] #[2,:] entire row
# print(eggs)

# task6
one_egg = eggs[ (eggs==1) ]
# print(one_egg)

# task7
cookies = recipes[2,:]
# print(cookies)

# task8
double_batch = cupcakes * 2
# print(double_batch)

# task9
grocery_list = cookies + double_batch
print(grocery_list)
# task10


