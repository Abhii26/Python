"""Ques5. Weather Activity Suggestion
Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)."""

weather = input("Enter the weather of your city: ").lower()

# METHOD: 1

if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Do Nothing")

# METHOD : 2

if weather == "sunny":
    activity= "Go for a walk"
elif weather == "rainy":
    activity= "Read a book"
elif weather =="snowy" :
    activity= "Build a snowman"
else:
    activity = "Do Nothing"
print (activity)