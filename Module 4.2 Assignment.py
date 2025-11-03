# Made by: Samuel Sidzyik
# Module 4.2 Assignment.py
# Start Date November 02, 2025
# This program uses a takes input from the user and converts the input from km to miles.
# I will be segmenting the code into functions according to Chapter 5 and using try catch statements for data validation from Chapter 6. Even though Chapter 6 wasn't listed in this module! lol

# I will not know actual conversion math. Had to get the calculation from here: https://www.rapidtables.com/convert/length/km-to-mile.html
# Also referenced Chapter 6 Program 6-29
# Rounding float: https://www.geeksforgeeks.org/python/how-to-get-two-decimal-places-in-python/

def GetTheKMs():
    distance_km = 0
    while distance_km == 0: # Keeps asking until a positive value is reached.
        try:
            distance_km = float(input('Enter the amount of Kilometers to be translated to miles:'))
            if distance_km <= 0: # I felt like not allowing negatives or zero
                print('Your entered value must be greater than 0.')
                distance_km = 0

        except ValueError: # Catches non numerical values
            print('You must enter numerical data only.')
            distance_km = 0

        except: # I don't know what this catches but putting it in to be safe. Found in 6-29 image
            print('Unkown Error Occurred.')
            distance_km = 0

    return distance_km

def DoTheMath(distance_km):
    distance_mi = distance_km / 1.609344
    return distance_mi

#Calls first function to get input KMs
distance_km = GetTheKMs()

#Calls second function to do the math translation
distance_mi = DoTheMath(distance_km)

print(f"The amount of miles calculated from {round(distance_km,2)} kilometers would be {round(distance_mi, 2)} miles.")