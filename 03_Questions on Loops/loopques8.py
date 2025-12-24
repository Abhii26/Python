""" Ques8. Prime Number Checker
Problem: Check if a number is prime."""

num = int(input("Enter the Number: "))

is_prime = True  # Taking a boolean value and bydefault True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print(f"{num} is Prime Number: ", is_prime)