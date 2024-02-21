#Exceeding the Requirements:
#added tire prices and the ability to go through with a purchase
#accepting the purchase prompts many more inputs and stores additional information on the file
#additional measures are implemented for resolving incorrect inputs
#some basic styling and formatting added

import math
from datetime import datetime

#gets the date
date = datetime.now()

#formatting
print("-------------------------------\nWlcome to the Tire Store (name tbd)\n-------------PRICE-------------\n1. standart: 5$/litre\n2. winter: 7$/litre\n3. NEW tire+ extra deluxe: 12$")

#measurment inputs
print("----------MEASURMENTS----------")
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#volume estimate calculation
volume = (math.pi * width ** 2 * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000000

#volume display
print("-------------VOLUME------------")
print(f"The approximate volume is {volume:.2f} litres")

#purchase input
print("------------PURCHASE-----------")
buyer = input("Would you like to make the purchase? (Y/N): ")


#purchase accepted check
if buyer.lower() == "y":
    name = input("Please provide your full name: ")
    phone = input("Please provide your mobile phone number: ")
    
    tireType = int(input("What type of tire are you interested in purchasing? (1/2/3): "))

    #in case of incorrect input ends the purchase process
    if tireType !=1 and tireType !=2 and tireType !=3:
        print("An unexpected error has occurred.")

        with open("volumes.txt", "at") as volumes_file:
            print(f"{date:%Y-%m-%d}, {width}, {aspectRatio}, {diameter}, {volume:.2f}, E", file=volumes_file)

    #if no incorrect input, continues
    else:
        amount = input("How many tires are you purchasing?: ")

        if tireType == 1:
            price = volume*5.0*float(amount)
        elif tireType == 2:
            price = volume*7.0*float(amount)
        elif tireType == 3:
            price = volume*12.0*float(amount)

        print(f"The total price for {amount} tires of {volume:.2f} litres volume is: {price:.2f}$.")

        with open("volumes.txt", "at") as volumes_file:
            print(f"{date:%Y-%m-%d}, {width}, {aspectRatio}, {diameter}, {volume:.2f}, Y, {name}, {phone}, {tireType}, {amount}, {price:.2f}", file=volumes_file)


#purchase declined check
elif buyer.lower() == "n":
    print("Okay. We hope to see you another day.")

    with open("volumes.txt", "at") as volumes_file:
        print(f"{date:%Y-%m-%d}, {width}, {aspectRatio}, {diameter}, {volume:.2f}, N", file=volumes_file)


#incorrect input check
else:
    print("An unexpected error has occurred.")

    with open("volumes.txt", "at") as volumes_file:
        print(f"{date:%Y-%m-%d}, {width}, {aspectRatio}, {diameter}, {volume:.2f}, E", file=volumes_file)