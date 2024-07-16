# USING EHILE LOOP

import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice([-1, 0, 1])

# Dictionaries to map choices to their respective values
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

while True:
    # Get the user's choice
    youstr = input("Enter your choice: ").lower()
    
    if youstr == 'q':
        print("Thank you for playing!")
        break
    elif youstr not in youdict:
        print("Invalid input, please enter 's', 'w', 'g', or 'q' to quit.")
        continue
    
    # Get the computer's choice
    computer = get_computer_choice()
    you = youdict[youstr]

    # Print the choices
    print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")
    
    # Determine the winner
    if computer == you:
        print("IT IS A DRAW")
    else:
        if (computer == -1 and you == 1):
            print("YOU WIN")
        elif (computer == -1 and you == 0):
            print("YOU LOSE")
        elif (computer == 1 and you == -1):
            print("YOU LOSE")
        elif (computer == 1 and you == 0):
            print("YOU WIN")
        elif (computer == 0 and you == -1):
            print("YOU WIN")
        elif (computer == 0 and you == 1):
            print("YOU LOSE")
        else:
            print("SOMETHING WENT WRONG")
