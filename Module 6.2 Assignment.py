# Made by: Samuel Sidzyik
# Module 6.2 Assignment.py
# Start Date November 17, 2025
# This program begins by creating a tuple. The tuple is then displayed.
# Then through iteration there is a complete sentence created. Finally, the order of
# the tuple is reversed and printed again.
# 


def main():
    States = ('Alabama','Alaska','Arizona','Tenessee','Mississippi','Washington',
              'Montana','Idaho','Maine','New Hampshire','Conneticut','Nevada',
              'New York','Massachutes','Virginia','West Virginia','Florida')
    print(States)
    PrintStatement(States)
    ReversedString = GetReverseString(States)
    print(ReversedString)

def GetReverseString(States):
    ReverseString = ""
    for State in States:
        ReverseString = State + " " + ReverseString
    return ReverseString

def PrintStatement(States):
    for State in States:
        print(f"I have not visited {State}.")

if __name__ == "__main__":
    main()