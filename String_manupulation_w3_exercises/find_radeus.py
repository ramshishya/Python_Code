# Write a Python program that calculates the area of a circle based on the radius entered by the user.

from math import pi

r=float(input("Enter radius for circle"))

area=pi * r ** 2

print(f"Circle Area:{area}")
