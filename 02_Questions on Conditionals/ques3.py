""" Ques3. Grade Calculator
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (60). """
score = int(input("Enter Your Grade Score: "))

# METHOD: 1
if score > 100 or score < 0:
    print("Invalid Grade!! \nPlease Verify Your Grade")
    exit()

if score >= 90 :
    grade = "A"
    print(grade)
elif score >= 80:
    grade = "B"
    print(grade)
elif score >= 70:
    grade = "C"
    print(grade)
elif score >= 60:
    grade = "D"
    print(grade)
else:
    grade = "F"
    print(grade)

# METHOD: 2

if score > 100 or score < 0:
    print("Invalid Grade")
else:
    if score >= 90 :
        grade = "A"
        print(grade)
    elif score >= 80:
        grade = "B"
        print(grade)
    elif score >= 70:
        grade = "C"
        print(grade)
    elif score >= 60:
        grade = "D"
        print(grade)
    else:
        grade = "F"
        print(grade)


