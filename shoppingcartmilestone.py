cart = [ ]
cart_items = " "
shopping_activity = " "
item_price = " "
cart_total = [ ]
item_index = " "

while shopping_activity != "5":
	print(" 1. Add new item\n 2. Display added items\n 3. Remove an item\n 4. Compute total\n 5. Quit")
	shopping_activity = input("what would you like to do? ")
	
	print()
	if shopping_activity == "1":
		cart_items = input ("what item would you like to add to the cart? ")
		item_price = float (input("what is the price of the item? "))
		print(f"{cart_items} has been added successfully ")
		print()
		cart.append(cart_items)
		cart_total.append(item_price)

	elif shopping_activity == "2":
		print("items in cart are: ")
		for i in range (len(cart)):
			cart_items = cart[i]
			item_price = cart_total[i]
			print(f"{(i+1)}. {cart_items} ${item_price:.2f} ")
			print()

	elif shopping_activity == "3":
		item_index = int(input ("what is the item's number? "))

		#first we print that the item has been removed
		#it is easier to do this before we actually remove the item, because it's going to be hard when the item is already gone from the list
		#you can print a specific item from a list by using list_name[index of the item]
		#but it counts from 0. cart[0] would print the first item, cart[1] would print the second item in teh list ect.
		#but here we use the index that the user input above named item_index
		#but we subtract 1 because the list counts from 0.
		print(f"{cart[item_index - 1]} has been removed.")

		#then we need to remove the item from the cart list and from the second list that has the price of the item
		#for this we use .pop() and put the index in the brackets.
		#which is again, item_index - 1.
		cart.pop(item_index - 1)
		cart_total.pop(item_index - 1)

	elif shopping_activity == "4":

		#now we need to add up every price in the second list and display the total
		#we can use sum() to add up all the numbers in a list.
		total_cost = sum(cart_total)

		#then we print the total and use :.2f to roand it to 2 decimal digits
		print(f"The total price of the items in the shopping cart is ${total_cost:.2f}")

	elif shopping_activity == "5":
			print("Goodbye. See you soon!")
	
	#i added an else statement that says it's a wrong input if the user tries to input anything except 1,2,3,4,5
	else:
		print("Incorrect activity input, please try again.")
