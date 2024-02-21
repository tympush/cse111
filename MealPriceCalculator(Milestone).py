childMealPrice = float(input("What is the price of a child's meal? "))
adultMealPrice = float(input("What is the price of an adult's meal? "))
childAmount = int(input("How many children are there? "))
adultAmount = int(input("How many adults are there? "))
taxRate = float(input("What is the sales tax rate? "))

subTotal = childAmount * childMealPrice + adultAmount * adultMealPrice
salesTax = subTotal * taxRate / 100
totalPayment = subTotal + salesTax

print(f"\nSubtotal: ${subTotal:.2f}")
print(f"Sales Tax: ${salesTax:.2f}")
print(f"Total: ${totalPayment:.2f}")

paymentAmount = float(input("\nWhat is the payment amount? "))
print(f"Change: ${paymentAmount - totalPayment:.2f}")