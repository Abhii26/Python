""" Ques7. Function with *args
Problem: Write a function that takes variable number of arguments and retums their sum."""

# Method 1 (Using Sum --> It is default method in python in which we can give multiple parameter for sum )

def sum_new(*args): # Here instead or args we can put any other but we dont do that bcz that is not good practice
    return sum(args)

print("Sum of Numbers are:",sum_new(1, 2, 3, 4, 5))



# Method 2 (Using Loop)

def sum_all(*args):
    x=0
    print(type(*args)) # It show error becoz *args does not produce one object — it unpacks into multiple objects
    print(type(args)) # Here we get tuple as a type 
    for i in args:
        x = x+i
    return x

print("Sum Of All No: ",sum_all(1, 2, 3))