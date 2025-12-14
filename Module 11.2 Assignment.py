# Made by: Samuel Sidzyik
# Module 11.2 Assignment.py
# Start Date December 14, 2025
# 
# Last assignment!!! Take an input and check for integer greater than 0.
# Run it both through a recursive and non-recursive function to print all values from 1 to (n).
#

# I haven't had the main function on top for the past couple assignments but I prefer to have it up here as it makes more sense to me for reading
def main():
    print("This is the recursive function")
    count_data = get_data()
    recursive_function(count_data)
    
    print("This is the non-recursive function")
    count_data = get_data()
    manual_function(count_data)

# This works by having a default value of 1 but will pass an increased value by 1 until it reaches the limit of the recursive function
def recursive_function(limit, current_place=1):
    if (current_place < limit):
        print(current_place, end=", ")
        current_place += 1
        recursive_function(limit,current_place)
    else:
        print(f"{current_place}\n")

# This works by counting until it reaches the limit value and printing its current place each time.
def manual_function(limit):
    current_place = 1
    while (current_place < limit):
        print(current_place, end=", ")
        current_place += 1
    print(f"{current_place}\n")

def get_data():
    # I used this function is module 5.2. Just copied it and removed unnecessary checks.
    return_value = "."
    while return_value == ".": # Keeps asking until a valid value passed
        try:
            return_value = input(f'Enter a number larger than 0.: ')
            if len(return_value) <= 0: # I won't allow blanks
                print('I will not allow blank entry.')
                return_value = "."
            elif len(return_value) > 2: # Just a quick limit to only have up to 99 on the count
                print("I'm limiting the number up to 99.")
                return_value = "."
            return_value = int(return_value)
            if return_value <= 0: # I won't allow zero or negatives
                print('I will not allow values less than 1.')
                return_value = "."

        except ValueError: # Catches non numerical values
            return_value = "."

        except: # I don't know what this catches but putting it in to be safe. Found in 6-29 image
            print('Unkown Error Occurred.')
            return_value = "."
    return return_value

if __name__ == "__main__":
    # I did this a few programs ago and have left it in. It doesn't hurt but I don't think it's necessary unless this program is getting called..
    main()