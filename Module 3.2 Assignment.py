# Made by: Samuel Sidzyik
# Module 3.2 Assignment.py
# Start Date October 29, 2025
# This program uses a while loop to determine how long it takes for an investment to double at a given interest rate.
# The input will be an annualized interest rate and the initial investment amount, and the output is the number of years it takes an investment to double.

# It's been a while since I've done real math. Was double checking my calculations at https://www.calculator.net/investment-calculator.html

# Start
#Initiate Variables
years = 0
StartingAmount = 1

#Grabs the user entered interest rate.
InterestRate = float(input("Enter current annualized interest rate: "))

#This turns an interest rate into a mathematical comparison. 5.5% = .0055. Adding 1 here means I don't have to add the starting amount back after multiplying interest.
InterestRate = (InterestRate/100) + 1

while StartingAmount < 2:
    StartingAmount *= InterestRate
    years += 1

# Gives answer.
print(f"It will take {years} years to double an investment at an annualized interest rate of {((InterestRate-1)*100):.1f}%.")
