""" Ques8. Function with **kwargs
Problem: Create a function that accepts any number of keyword arguments and prints them in the format
key: value."""

def showcase(**kwargs):
    for key, value in kwargs.items():
        print(f"Keys: {key}\n Value: {value}" )

showcase(name ="Parrot", color ="Green")