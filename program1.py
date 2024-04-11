'''
Katellyn Hyker
Chapter 3 Project 1
A program to recieve the input of three sides of a triangle and determine if the triangle is equilateral
An equilateral triangle is a triangle where all three sides are the same length

'''

# Recieve sides of triangle 
first_side = int(input("Enter the first side of the triangle: "))
second_side = int(input("enter the second side of the triangle: "))
third_side = int(input("Enter the third side of the triangle: "))

# If statement determining if the triangle is equilateral
if first_side == second_side and second_side == third_side:
    print("The triangle is an equilateral triangle.")
else:
    print("The triangle is not an equilateral triangle.")
