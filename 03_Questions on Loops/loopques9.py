""" Ques9. List Uniqueness Checker
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the
duplicate element.
items =["apple", "banana", "orange" , "apple", "mango"]"""

items =["apple", "banana", "orange" , "banana", "mango"]

# Method 1: Simple approach (High Time Complexity: 0(n**2))
# This is fine for small lists, but inefficient for large ones.

for i in items:
    if items.count(i) > 1:   # list.count() runs in O(n) time
        break
print("Duplicate Item is: ",i)

#-----------------------------------------------------------------------------------------------------

# Method 2: Using set() (Low Time Complexity: 0(n))

duplicate = set()

for i in items:
    if i in duplicate:    # Lookup in a set is O(1)
        print("Duplicate Item is: ",i)
    else:
        duplicate.add(i)

