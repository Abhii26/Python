""" Ques4. Reverse a String
Problem: Reverse a string using a loop."""

# Method 1 : Basic Way (using Only Loop)

x = input("Enter a String: ")
reverse_string = ""

for i in x:
    reverse_string = i + reverse_string  # here if we do reverse_string = reverse_string + i then o/p = x(entered string)   
                                        # but we have done reverse_string = i + reverse_string -> o/p = reverse string                 
print(reverse_string)

#-----------------------------------------------------------------------------------------------------------------

# Method 2 : Simple Way (using slicing)

x = input("Enter a String: ")

for i in x[::-1]:
    print(i, end="")

#------------------------------------------------------------------------------------------------------------------------

# Method 3 : Alternative Manual Reverse Loop (without slicing)

# Explaination :- How range() works

# start → where to begin (length-1)
# stop → where to stop (excluded) (-1([excluded], means upto 0 )
# step → how much to move each time (-1, means in right -> left [opposite])

x = input("Enter a String: ")
length = len(x) 

for i in range(length-1, -1, -1): # start from last index to 0
    print(x[i], end="")  # here x[i] means you are taking result through indexing
                         # assume string is 'hello'
                         # x[4] → o
                         # x[3] → l
                         # x[2] → l
                         # x[1] → e
                         # x[0] → h 