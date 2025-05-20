weight = 8.4

#Ground shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20

elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20
#print(cost_ground)
cost_ground_premium= 125.00
#print(cost_ground_premium)

#Drone  shipping

drone_weight = 1.5
if drone_weight <= 2:
  cost_drone = drone_weight * 4.50
elif drone_weight <= 6:
  cost_drone = drone_weight * 9.00
elif drone_weight <= 10:
  cost_drone = drone_weight * 12.00
else:
  cost_drone = drone_weight * 14.25 
print(cost_drone)

