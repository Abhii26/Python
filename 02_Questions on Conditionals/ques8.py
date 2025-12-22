""" Ques8. Password Strength Checker
Problem: Check if a password is "Weak", "Medium", or 'Strong'. Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)."""

password = input("Enter your password : ")
new_pass = len(password)

if new_pass <6:
    text= "Weak"
elif new_pass <11:
    text= "Medium"
else:
    text= "Strong"

print(text)