from datetime import datetime

today = datetime.now()
#today = datetime.date.today()
weekDay = today.weekday()

subtotal = 0
price = 1

price = float(input("Price: "))
while price != 0:
    amount = float(input("Amount: "))
    subtotal += price*amount
    price = float(input("Price: "))


if weekDay == 1 or weekDay == 2:

    if subtotal >= 50:
        subtotal = subtotal*0.9
        print(f"Discounted amount: {subtotal:.2f}")
    
    else:
        print(f"You need {50-subtotal:.2f} to receive the discount")

tax = subtotal*0.06
print(f"Sales Tax: {tax:.2f}")
total = subtotal + tax
print(f"Total Amount: {total:.2f}")