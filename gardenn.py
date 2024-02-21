# Author: Evangelis Albesa

import time

INVENTORY = []
STATES = []

def chooseFromArray(options):
    choice = ""
    while choice not in options:
        choice = input(f">>Which path will you choose? {options}: ")
        choice = choice.upper()
    return choice

def playAgain():
    choice = input(
        "Do you want to play again? (yes or y to continue playing): ")
    choice = choice.lower()
    if choice == "yes" or choice == "y":
        return garden
    else:
        return quit

def quit():
    print()
    print("** Thanks for playing **")
    exit(0)

def win():
    print("You win!")
    return playAgain()

def lose():
    print("You lose!")
    return playAgain()

def dragon():
    print("You are standing in front of a sleeping dragon.")
    time.sleep(2)
    if "ROSE" not in INVENTORY:
        print("Oh no! The dragon awakes and burns you to a cinder!")
        print()
        return lose
    else:
        print("The dragon's eyes slowly open, and he regards you warily.")
        print()
        choice = chooseFromArray(["ROSE", "RUN"])
        if choice == "RUN":
            print("You run, but the dragon is faster.")
            print()
            return lose
        else:
            print("The dragon takes the ROSE from you with his enormous claw and then flies away.")
            print()
            return win

def cottage():
    options=["LEFT", "RIGHT"]
    print("You are standing in front of a small cottage.")

    if "COTTAGE_OPEN" not in STATES:
        print("The front door appears to be locked.")
        if "KEY" in INVENTORY:
            print("...but you have a key. Do you want to UNLOCK it?")
            options.append("UNLOCK")
    else:
        print("The front door is open!")
        options.append("AHEAD")
    
    print("To your LEFT is a mailbox with the flag up.")
    print("To your RIGHT is a path leading back to the garden.")
    print()
    choice = chooseFromArray(options)
    if (choice == "LEFT"):
        return mailbox
    elif choice == "RIGHT":
        return garden
    elif choice == "UNLOCK":
        STATES.append("COTTAGE_OPEN")
        INVENTORY.remove("KEY")
        return cottage
    elif choice == "AHEAD":
        return kitchen

def kitchen():
    options = ["BACK"]
    print("You are standing in a small kitchen")
    if "FLASHLIGHT_FOUND" not in STATES:
        print("On the counter is a FLASHLIGHT.")
        options.append("FLASHLIGHT")
    else:
        print("You find nothing of interest.")
    print()
    choice = chooseFromArray(options)
    if choice == "FLASHLIGHT":
        STATES.append("FLASHLIGHT_FOUND")
        INVENTORY.append("FLASHLIGHT")
        return kitchen
    else:
        return cottage

def cave():
    if "FLASHLIGHT" not in INVENTORY:
        print("You are standing in a dark cave.")
        print("Did you forget your flashlight?")
        print()
        choice = chooseFromArray(["BACK"])
        return garden
    elif "ROSE_FOUND" not in STATES:
        print("You ared standing in a cave.")
        print("In front of you, lying upon an altar of stone, lies a single, red ROSE.")
        print()
        choice = chooseFromArray(["ROSE", "BACK"])
        if choice == "ROSE":
            INVENTORY.append("ROSE")
            STATES.append("ROSE_FOUND")
            return cave
        else:
            return garden
    else:
        print("You are standing in an empty cave.")
        print()
        choice = chooseFromArray(["BACK"])
        return garden

def mailbox():
    print("You look inside the mailbox.")
    if "LETTER_READ" not in STATES:
        print("You find a letter. It's addressed to you!")
        print("Would you like to READ it?")
        print()
        choice = chooseFromArray(["READ", "BACK"])
        if choice == "READ":
            STATES.append("LETTER_READ")
            return letter
        else:
            return cottage
    else:
        print("The mailbox is empty.")
        choice = chooseFromArray(["BACK"])
        return cottage

def letter():
    print("The letter reads:")
    print("Congratulations! You have won a million dollars!")
    print()
    time.sleep(2)
    print("The letter also contains a KEY.")
    print("A KEY has been added to your inventory.")
    INVENTORY.append("KEY")
    return mailbox

def garden():
    print("You are standing in a garden full of beautiful flowers and very fragrant.")
    print("AHEAD of you, not far in the distance, is a large sleeping dragon, snoring loudly.")
    print("To your LEFT is a path leading to a small cottage.")
    print("To your RIGHT is a path leading to a dark cave.")
    print()
    choice = chooseFromArray(options=["AHEAD", "LEFT", "RIGHT"])
    if (choice == "AHEAD"):
        return dragon
    elif (choice == "LEFT"):
        return cottage
    else:
        return cave

def main():
    print()
    print("Welcome to the Adventure game")
    print()
    location = garden
    while True:
        print("--------------------------------")
        location = location()

if __name__ == "__main__":
    main()