'''
Katellyn Hyker
Chapter 3 Project 9
A program that recieves a series of numbers and upon enter key prints the sum of numbers and average

'''
#Set up starting values
count = 0
user_sum = 0

#Prompt for the first number
numbers = input("Enter a number or hit enter to stop: ")

#Calculate the sum, count the number of numbers and prompt the user to enter an input
while numbers != "":
    number = float(numbers)
    user_sum += number
    count += 1
    numbers = input("Enter a number or hit enter to stop: ")

#Print the results
print(f'Your sum of numbers is {user_sum} and your average is {user_sum/count}')