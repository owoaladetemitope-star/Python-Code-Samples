#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Your Name: Barakat Owoalade
# Date: February 5, 2026
# This program contains answers for Problems 1 through 7 css 225 module 3 lab acitivty

# Problem 1
# This program prints Hello World

print("Hello World")

# Problem 2
# This program asks the user for their name and greets them

name = input("Enter your name: ")
print("Hello " + name)

# Problem 3
# This program only greets you and your instructor by name


if name.lower() == "barakat" or name.lower() == "instructor":
    print("Hello " + name)
else:
    print("Hello student")

# Problem 4
# This program calculates the area of a circle

radius = float(input("Enter the radius of the circle: "))

area = 3.14159 * radius * radius

print("The area of the circle is " + str(area))


# Problem 5
# This program calculates miles per gallon (MPG)

miles = float(input("Enter the number of miles driven: "))
gallons = float(input("Enter the number of gallons used: "))

mpg = miles / gallons

print("Your car gets " + str(mpg) + " miles per gallon.")


# Problem 6
# This program converts Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("The temperature in Celsius is " + str(celsius))

# Problem 7
# This program calculates what day you will return from vacation

start_day = int(input("Enter the starting day number (0-6): "))
length_of_stay = int(input("Enter the number of nights you will stay: "))

return_day = (start_day + length_of_stay) % 7

print("You will return on day number " + str(return_day))


# In[ ]:





# In[ ]:





# In[ ]:




