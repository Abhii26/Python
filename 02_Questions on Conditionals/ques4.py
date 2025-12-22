"""Ques4. Fruit Ripeness Checker
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)"""

fruit = input("Enter the fruit: ").lower()

# This is called string interpolation.
# Method 1:
color = input(f"Enter the color of {fruit}: ").lower()
 # f"..." allows you to inject variables into strings, {fruit} is replaced with the actual value

# Method 2:
newcolor = input("Enter the color of {} : ".format(fruit)).lower()
# here we use .format() method for string interpolation


# WE CAN USE BOTH color or newcolor, BOTH ARE CORRECT

if fruit == "banana":
    if color == "green":
        print("UnRipe")
    elif color == "yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
else:
    print("Sorry!! I don't have info about that fruit")
    

