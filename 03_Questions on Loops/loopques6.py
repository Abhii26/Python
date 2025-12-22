""" Ques6. Factorial Calculator
Problem: Compute the factorial of a number using a while loop."""

num = int(input("Enter the Number: "))
# Method 1 
fact = 1
i= 1

while i <= num:
    fact *= i
    i = i+1 # Here basically we are doing like 1*2*3*4*5
    
print("Factorial of the given number is : ",fact)

#-------------------------------------------------------------------------------------------

# Method 2
fact = 1

while num>0:
    fact *= num
    num  -= 1  # Here basically we are doing like 5*4*3*2*1

print("Factorial of the given number is : ",fact)