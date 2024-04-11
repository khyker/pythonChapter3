'''
Katellyn Hyker
Chapter 3 Project 2
A program that recieves an input of three sides of a triangle and determine if the triangle is a right triangle

'''
import math

# Recieve sides of triangle 
a = int(input("Enter the side A of the triangle: "))
b = int(input("enter the side B of the triangle: "))
c = int(input("Enter the side C of the triangle: "))

# Determine if it is a right triangle and print the according message
if c == math.sqrt((b**2)+(a**2)):
    print("This triangle is a right triangle.")
else:
    print("This triangle is not a right triangle.")