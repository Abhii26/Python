""" Ques3. Multiplication Table Printer
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration."""

n = int(input("Enter The Number: "))

for i in range(1,11):
    if i == 5:
        continue   # Here i can use 'pass' also as it do nothing when i==5, but it only useful if print() is in else: statement
    else:
        print(n, "x", i, "=", n*i )

#----------------------------------------------------------------------------------------------------------------------------

# Here Only contine is valid as continue skip the current iteration so it skip i==5 teration, and print remaining all

for i in range(1,11):
    if i == 5:
        continue # Here if i use pass instead of continue it will print the value of 5 as print is used in if statement
    print(n, "x", i, "=", n*i )