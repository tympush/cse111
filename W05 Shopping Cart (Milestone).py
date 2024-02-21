shoppingCartItems = []
shoppingCartPrices = []
continueList = True

while 1 == 1:
    itemInput = input("\nWhat item would you like to add? ").lower()

    if itemInput.lower() == "quit":
        break

    shoppingCartItems.append(itemInput)
    priceInput = float(input(f"What is the price of '{itemInput}'? "))
    shoppingCartPrices.append(priceInput)
    print(f"'{itemInput}' has been added to the cart.")

    print("\nThe contents of the shopping cart are:")
    for i in range(len(shoppingCartItems)):
        print(f"{i+1}. {shoppingCartItems[i]}")