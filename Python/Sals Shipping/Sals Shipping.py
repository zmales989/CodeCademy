weight = 95

#Ground Shipping 
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)
      
cost_ground_premium = 125.00

print("Ground Shipping Premimium $", cost_ground_premium)

#Drone shipping
if weight <= 2:
  cost_air = weight * 4.50 + 0
elif weight <= 6:
  cost_air = weight * 9 + 0
elif weight <= 10:
  cost_air = weight * 12 + 0
else:
  cost_air = weight * 14.25 + 0

print("Air Shipping $", cost_air)



