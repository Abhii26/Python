""" Ques5. Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character."""

x = input("Enter a String: ")

for i in x:
    if x.count(i) == 1: # here x.count(i) means “Count how many times the character i appears in the string x.”
        print(i)
        break   # here we used break bcoz if we get a character with 0 repetition then why we have to check other substring 
                # as in question we have given find the first non-repeated character. So We Get That
                # break is used for optimization 