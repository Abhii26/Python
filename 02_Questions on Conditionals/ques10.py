""" Ques10. Pet Food Recommendation
Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)."""

petage = int(input("Enter Pet Age: "))
pettype = input("Enter Your Pet Type: ").capitalize().strip() # strip() remove unwanted space from start and end.

if pettype == "Dog":
    if petage < 2:
        print(f"Your {pettype} need Puppy Food")
    else:
        print(f"Your {pettype} need Adult Food")
elif pettype == "Cat":
    if petage > 5:
        print(f"Your {pettype} need Senior Cat Food")
    else:
        print(f"Your {pettype} need Kitten Food")
else:
    print(f"No Information about {pettype} Sorry!!")    

