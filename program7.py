'''
Katellyn Hyker
Chapter 3 Project 7
Display a salery schedule in tabular format for teachers in a school district

'''
# Inputs
start_salary = int(input("Enter the starting salary: "))
percentageIncrease = int(input("Enter the percentage increase: "))
numYears = int(input("Enter the number of years: "))

def calcSalary(start_salary, percentageIncrease, numYears):
    print("%-10s%-4s" % ("Year", "Salary"))
    for years in range(1, numYears):
        salaryIncrease = start_salary*percentageIncrease
        salary = start_salary + salaryIncrease
        start_salary = salary
        print("%-10s%-4s" %(years, salary))

calcSalary(start_salary, percentageIncrease, numYears)