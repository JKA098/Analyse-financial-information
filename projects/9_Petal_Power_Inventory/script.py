# task 1
import codecademylib3
import numpy as np
import pandas as pd
# task 2
inventory = pd.read_csv('inventory.csv')
print(inventory)
# task 3
staten_island = inventory.head(10)

# task 4
product_request = staten_island.product_description

# task 5
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
# print(seed_request)

# task 6
inventory['in_stock'] = inventory.apply(
  lambda n: True if n.quantity > 0 else False, axis=1)
# print(inventory['in_stock'])
# task 7
inventory['total_value'] = inventory.apply(
  lambda n: n.price * n.quantity , axis=1)

# task 8

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
# print(combine_lambda)
# task 9
inventory['full_description'] = inventory.apply(
  combine_lambda, axis=1
)



