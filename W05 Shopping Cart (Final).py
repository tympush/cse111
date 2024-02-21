#Creativity:
#Added the ability to select a quantity for how many items you are buying, which is reflected in every action (when adding, when removing, when replacing, and is counted into the total).
#Added a new action to replace an item, which is like the remove action but it allows you to add a new item instead that is added to that index in the list.
#Lastly, added some better formatting and new errors that allow you to try again in several places (like the cart being empty or you not being allowed to take 0 or less of an item).

shoppingCartItems = []
shoppingCartPrices = []
shoppingCartQuantity = []
continueList = True

print("Welcome to the Shopping Cart Program!")

while 1 == 1:
    print("\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Replace item\n5. Compute total\n5. Quit")
    actionInput = input("Please enter an action: ")

    if actionInput == "1":
        itemInput = input("\nWhat item would you like to add? ").capitalize()
        shoppingCartItems.append(itemInput)
        priceInput = float(input(f"What is the price of '{itemInput}'? "))
        shoppingCartPrices.append(priceInput)

        while 1 == 1:
            quantityInput = int(input(f"How much '{itemInput}' are you buying? "))

            if quantityInput <= 0:
                print("You can't take 0 or less of an item")

            else:
                shoppingCartQuantity.append(quantityInput)
                break

        print(f"{quantityInput}x '{itemInput}' added to the cart.")

    elif actionInput == "2":

        if len(shoppingCartItems) == 0:
            print("\nThe cart is empty.")

        else:
            print("\nThe contents of the shopping cart are:")
            for i in range(len(shoppingCartItems)):
                print(f"{i+1}. {shoppingCartItems[i]} x{shoppingCartQuantity[i]} - ${float(shoppingCartQuantity[i]) * shoppingCartPrices[i]:.2f}")

    elif actionInput == "3":
        print(f"\nThere are {len(shoppingCartItems)} items in the shopping cart.")

        if len(shoppingCartItems) == 0:
            print("There is nothing to remove.")

        else:
            while 1 == 1:
                itemNumber = int(input("Which item would you like to remove? "))

                if itemNumber < 1 or itemNumber > len(shoppingCartItems):
                    print("Sorry, that is not a valid item number.")
                
                else:
                    break
        
            print(f"{shoppingCartQuantity[itemNumber-1]}x '{shoppingCartItems[itemNumber-1]}' removed.")
            shoppingCartItems.pop(itemNumber-1)
            shoppingCartPrices.pop(itemNumber-1)
            shoppingCartQuantity.pop(itemNumber-1)

    elif actionInput == "4":
        print(f"\nThere are {len(shoppingCartItems)} items in the shopping cart.")

        if len(shoppingCartItems) == 0:
            print("There is nothing to replace.")

        else:
            while 1 == 1:
                itemNumber = int(input("Which item would you like to replace? "))

                if itemNumber < 1 or itemNumber > len(shoppingCartItems):
                    print("Sorry, that is not a valid item number.")
                
                else:
                    break
            
            removedItem = shoppingCartItems[itemNumber-1]
            removedQuantity = shoppingCartQuantity[itemNumber-1]
            shoppingCartItems.pop(itemNumber-1)
            shoppingCartPrices.pop(itemNumber-1)
            shoppingCartQuantity.pop(itemNumber-1)

            itemInput = input("What item would you like to add instead? ").capitalize()
            shoppingCartItems.insert(itemNumber-1,itemInput)
            priceInput = float(input(f"What is the price of '{itemInput}'? "))
            shoppingCartPrices.insert(itemNumber-1,priceInput)

            while 1 == 1:
                quantityInput = int(input(f"How much '{itemInput}' are you buying? "))

                if quantityInput <= 0:
                    print("You can't take 0 or less of an item")

                else:
                    shoppingCartQuantity.insert(itemNumber-1,quantityInput)
                    break

            print(f"{removedQuantity}x '{removedItem}' replaced by {quantityInput}x '{itemInput}'.")
    
    #elif actionInput == "5":
    #    print(f"\nThe total price of the items in the shopping cart is {sum(shoppingCartPrices):.2f}")

    elif actionInput == "5":
        total = 0.0
        for i in range(len(shoppingCartItems)):
            total += (shoppingCartPrices[i] * float(shoppingCartQuantity[i]))
        print(f"\nThe total price of the items in the shopping cart is {total:.2f}")

    elif actionInput == "6":
        print("\nThank you. Goodbye.")
        break
    
    else:
        print("\nSorry, that is not a valid input.")