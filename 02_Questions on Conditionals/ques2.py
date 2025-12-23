""" Ques2 Movie Ticket Pricing 
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday."""

# METHOD 1:
day = input("Enter The Day: ").lower()
age = int(input("Enter Your Age: "))
price = 12 if age >= 18 else 8       # Dynamically changing price using if else

if day == "wednesday":
    #price = price - 2
    price -= 2
    print("Your Ticket Price is $",price)

else: 
    print("Your Ticket Price is $",price)


# METHOD 2:

day = input("Enter The Day: ").lower()
age = int(input("Enter Your Age: \n"))  #\n  for the next line so i can get input in the next line

#if i remove lower() function then if have do like this: if day == "wednesday" or day == Wednesday: 
if (day == "wednesday"): 
    print("You Get $2 Discount")
    if age > 17 :
        print("YoUr Ticket Price is of $10")
    else:
        print("Your Ticket Price is of $6")

else:
    if age > 17 :
        print("YoUr Ticket Price is of $12")
    else:
        print("Your Ticket Price is of $8")



