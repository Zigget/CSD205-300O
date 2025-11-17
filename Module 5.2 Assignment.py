# Made by: Samuel Sidzyik
# Module 5.2 Assignment.py
# Start Date November 16, 2025 (last minute, I know)
# This program uses a takes multiple inputs from the user to create and address in a text file.
# 

# Got the filename limiters from here: https://en.wikipedia.org/wiki/Filename
# Got the character list check from here: https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string

def main():
    # Prompt and validate Data
    filename = GetData("a File Name")
    username = GetData("your Name")
    address = GetData("your Address")
    phone = GetData("your Phone Number")

    # Create file and populate
    filename = CreateTheFile(filename, username, address, phone)
    filecontents = ReadTheFile(filename)

    # Print for validation
    print(f"The file contents consists of: {filecontents}")

def GetData(DataType):
    returntext = "."
    badcharacters = [".","/",":","?","#","*","|","\"","\\","<",">",",",";","="," "]
    while returntext == ".": # Keeps asking until a valid value passed
        try:
            returntext = (input(f'Enter {DataType}.: '))
            if len(returntext) <= 0: # I won't allow blanks
                print('I will not allow blank entry.')
                returntext = "."
            elif len(returntext) >= 25: # I won't allow unlimited entry. Good for preventing SQL injections I think
                print('I will not allow unlimited entry. Abbreviate if necessary.')
                returntext = "."
            elif any(x in returntext for x in badcharacters) and DataType == "a File Name": #Used in Filenames
                print('Do not use special characters or spaces in filenames.')
                returntext = "."
            elif returntext == "your Phone Number" and len(returntext) != 10: #This doesn't validate the way I hoped....
                int(returntext) # Prompts Value Error.
                print("Your phone number must be 10 digits.")
                returntext = "."

        #I'm generous with entry for name and address. Real life scenario I'd do a lot more data validation with regex and address validation with imports.

        except ValueError: # Catches non numerical values
            print('For you phone, only enter 10 digits no spaces, periods, or hyphens. i.e. 555-123-6789 should be entered as 5551236789.')
            returntext = "."

        except: # I don't know what this catches but putting it in to be safe. Found in 6-29 image
            print('Unkown Error Occurred.')
            returntext = "."

    return returntext

def CreateTheFile(filename, username, address, phone):
    filename = (f"{filename}data.txt")
    with open(filename, 'w') as newfile:
        newfile.write(f"{username},{address},{phone}")
    return filename

def ReadTheFile(filename):
    with open(filename, 'r') as newfile:
        filecontents = newfile.readline()
    return filecontents

if __name__ == "__main__":
    main()