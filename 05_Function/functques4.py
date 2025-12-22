""" Ques4. Function Retuming Multiple Values
Problem: Create a function that retums both the area and circumference of a circle given its radius."""

from math import pi

def circle(r):
    circum = 2 * pi * r 
    area = pi * r** 2
    return circum, area

x,y = circle(5)
c = round(x,2) # round() function is used to round off number upto desired places
a = f"{y:.2f}" # We can round off number using f-string or .format --> (a= "{.:2f}.format(y)" 
print("Cicumference of circle: ", c, "Area of circle: ", a)