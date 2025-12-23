""" Ques6. Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)."""

dist = int(input("Enter Your Distance: "))

if dist<3:
    mode = "Walk"
elif dist < 16:
    mode = "Bike"
else:
    mode = "Car"

print(mode)