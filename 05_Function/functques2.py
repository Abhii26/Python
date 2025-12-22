""" Ques2. Function with Muttiple Parameters
Problem: Create a function that takes two numbers as parameters and returns their sum."""

# Method 1: Taking Input From Users

# def sum_of_num():
#     a = int(input("Enter The First Number: "))
#     b = int(input("Enter The Second Number: "))
#     c = a+b
#     return c

# x = sum_of_num()
# print("The Sum of Numbers are: ",x)

# Method 2: Without User Input

def sum_of_numbers(a,b):
    return a+b

y = sum_of_numbers(5,6)
print("The Sum of Numbers are: ",y)
    