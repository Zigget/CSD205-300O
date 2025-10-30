# Made by: Samuel Sidzyik
# Module 2.2 Assignment.py
# Start Date October 27, 2025
# This program calculates the cost of fiber cable based user provided length and conditional rate based on length entered

# I disabled copilot the code is still autopopulating more than I like. IntelliSense? Maybe this is normal and my work has their stuff locked down? Distracting.

# Start
import os
import time

# Greeting. I added the get os name. We use this to check server names at work.
print(f"Hello {os.getlogin()}.")
time.sleep(1) #You always add unnecessary pauses to allow yourself to refactor later and improve timing.

#*insert Jim Carey face. Cable Guy!!!!
print("We will be calculating the cost of installing fiber optic cable for Cable Guy Co.") 
time.sleep(1)

#Basic variable assignment.
cablelength = int(input("How many feet of cable will be installed?: "))
#time.sleep(1) #removed to speed up user experience. lol. If I reuse this code a couple more times I can claim real refactoring improvements.

#Basic Math now with conditionals. I've never heard of the walrus operator until now. It is nice finding tidbits like this.
if cablelength <= 100:
    totalcost = cablelength * (rate := 0.87) #Standard rate.
elif 100 < cablelength <= 250:
    totalcost = cablelength * (rate := 0.80) #Bulk discount.
elif 250 < cablelength <= 500:
    totalcost = cablelength * (rate := 0.70) #Bulkier Discount.
else:
    totalcost = cablelength * (rate := 0.50) #Bulkiest Discount.

#No need to wait between calculation and printing.
#Print 2 decimal places using ;,.2f. I knew this from previous lessons but used google's prompt answer to get how to do it again
print(f"The total cost for installing {cablelength} feet of cable at a rate of ${rate:,.2f} is ${totalcost:,.2f}.")