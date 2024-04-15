'''
Katellyn Hyker
Chapter 3 Project 6
Write a program so the user can specify number of iterations.
Pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...

'''
def calcPi():
    pi_over_4 = 0
    iterations = int(input("Enter the number of iterations: "))

    for x in range(iterations):
        pi_over_4 += ((-1) ** x) * (4 / (2*x +1))

    return pi_over_4

print(f'Pi/4 is: {round(calcPi(), 2)}')