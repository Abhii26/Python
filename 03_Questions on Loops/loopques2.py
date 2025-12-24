""" Ques2. Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n."""

n = int(input("Enter the given number: "))
evensum = 0

for i in range(0,n+1):
    if i%2==0:
        evensum += i  #(evensum = evensum + i)
print(f"The Even Sum Of Number Upto {n} = ",evensum)
