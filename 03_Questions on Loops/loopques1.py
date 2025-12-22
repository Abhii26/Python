""" Ques1. Counting Positive Numbers
Problem: Given a list of numbers, count how many are positive.
    numbers :-  [1, -2, 3, -4, 5, 6, -7, -8, 9, 10] """

numbers =  [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]


# METHOD: 1 (Full Approach Using append()) 

positiveno = list()

for i in numbers:
    if i > 0:
        positiveno.append(i)
        # print(positiveno)   # It can be used to check the no.. is filling or not (for checking purpose)
        
print("Total Postive Numbers =", len(positiveno))


# METHOD: 2 (Simple Approach)

postive_number_count = 0
for x in numbers:
    if x > 0:
        postive_number_count += 1

print("Total Postive Numbers =",postive_number_count) 