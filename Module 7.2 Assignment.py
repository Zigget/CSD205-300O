# Made by: Samuel Sidzyik
# Module 7.2 Assignment.py
# Start Date November 28, 2025
# 
# This takes the name input from the user and splits it by the space before taking the first char and making it upper with a period after.


def main():
    full_name = input("Enter your first, middle, and last name: ")
    name_parts = full_name.split() # Splits on spaces
    initials = ""
    for part in name_parts:
        initials += part[0].upper() + ". " # indexing starts on 0. Grabs first char of each part of the name
    print("Your initials are:", initials.strip())


if __name__ == "__main__":
    main()