""" Ques7. Coffee Customization
Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso."""

size = input("Enter The Size of Coffee: ").capitalize()

extra_shot_input = input("Extra Shot of espresso: ").lower().strip() # strip() remove unwanted space from start and end.
extra_shot = extra_shot_input in ("true", "t", "yes", "y") # It checks whether a value exists inside a sequence (tuple, list, string, set).

if extra_shot :
    coffee = size + " coffee with extra shot of espresso"
else :
    coffee = size + " coffee"

print(coffee)

