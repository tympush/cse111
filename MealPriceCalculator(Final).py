#I added more items like drinks and deserts, and reorganised the inputs a bit to make it clearer for the user, as well as displaying the subtotals for each item category.
#I also added a charity donation option and an option to leave your change as a tip at the end.

print("Menu:")
childMealPrice = float(input("What is the price of a child's meal? "))
adultMealPrice = float(input("What is the price of an adult's meal? "))
childDrinkPrice = float(input("What is the price of a child's drink? "))
adultDrinkPrice = float(input("What is the price of an adult's drink? "))
childDessertPrice = float(input("What is the price of a child's dessert? "))
adultDessertPrice = float(input("What is the price of an adult's dessert? "))

print("\nOrder:")
childMealAmount = int(input("How many child's meals are you ordering? "))
adultMealAmount = int(input("How many adult's meals are you ordering? "))
childDrinkAmount = int(input("How many child's drinks are you ordering? "))
adultDrinkAmount = int(input("How many adult's drinks are you ordering? "))
childDessertAmount = int(input("How many child's desserts are you ordering? "))
adultDessertAmount = int(input("How many adult's desserts are you ordering? "))

taxRate = float(input("\nWhat is the sales tax rate? "))

charityLoop = True
print("")
while(charityLoop == True):
    charityAnswer = input("Do you want to donate to charity? (yes/no): ")
    if(charityAnswer.lower() == "yes"):
        charityDonation = float(input("How much do you want to donate? "))
        print("Thank you for your donation!\n")
        charityLoop = False
    elif(charityAnswer.lower() == "no"):
        print("Okay.\n")
        charityLoop = False
    else:
        print("Incorrect Input, try again.")

mealTotal = childMealAmount * childMealPrice + adultMealAmount * adultMealPrice
drinkTotal = childDrinkAmount * childDrinkPrice + adultDrinkAmount * adultDrinkPrice
dessertTotal = childDessertAmount * childDessertPrice + adultDessertAmount * adultDessertPrice
subTotal = mealTotal + drinkTotal + dessertTotal
salesTax = subTotal * taxRate / 100
totalPayment = subTotal + salesTax

print(f"Meal Total: ${mealTotal:.2f}")
print(f"Drink Total: ${drinkTotal:.2f}")
print(f"Dessert Total: ${dessertTotal:.2f}")
print(f"Subtotal: ${subTotal:.2f}")
print(f"Sales Tax: ${salesTax:.2f}")
print(f"Total: ${totalPayment:.2f}")

if(charityAnswer.lower() == "yes"):
    print(f"\nCharity Donation: ${charityDonation:.2f}")
    totalPayment = totalPayment + charityDonation
    print(f"Total + Charity: ${totalPayment:.2f}")

paymentAmount = float(input("\nWhat is the payment amount? "))
print(f"Change: ${paymentAmount - totalPayment:.2f}")

tipLoop = True
print("")
while(tipLoop == True):
    tipAnswer = input("Do you want to leave the change as a tip? (yes/no): ")
    if(tipAnswer.lower() == "yes"):
        print("Thank you!")
        tipLoop = False
    elif(tipAnswer.lower() == "no"):
        print("Okay.")
        tipLoop = False
    else:
        print("Incorrect Input, try again.")