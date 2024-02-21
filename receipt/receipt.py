# Exceeding the Requirements
# added 2 discounts
# 10% if it's Tuesday or Wednesday
# 10% if the time is before 11am
# they can stack for a 20% discount

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
        
    
    return dictionary

def main():
    #1
    print("Inkom Emporium\n")

    try: #9
        products_dict = read_dictionary("products.csv", 0) #2

        #2
        with open("request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)
            next(reader)

            numItems = 0 #3
            subtotal = 0 #4

            for row_list in reader:
                try: #9
                    print(f"{products_dict[row_list[0]][1]}: {row_list[1]} @ {products_dict[row_list[0]][2]}")

                    numItems += int(row_list[1]) #3
                    subtotal += float(products_dict[row_list[0]][2]) * float(row_list[1]) #4

                except KeyError as key_error: #9
                    print(f"Error: unknown product ID in the request.csv file {key_error}") #9

        #3
        print(f"\nNumber of Items: {numItems}")
        #4
        print(f"Subtotal: {subtotal:.2f}")

        #exceeding requirements
        current_date_time = datetime.now()
        discount = 0

        if current_date_time.weekday() == 1 or current_date_time.weekday() == 2:
            discount += 0.1

        if current_date_time.hour < 11:
            discount += 0.1
        
            
        subtotal = subtotal * (1-discount)
        print(f"Discount: {discount * 100:.0f}%\nDiscounted Subtotal: {subtotal:.2f}")

        #5
        print(f"Sales Tax: {subtotal*0.06:.2f}")
        #6
        print(f"Total: {subtotal*1.06:.2f}")
        #7
        print("\nThank you for shopping at the Inkom Emporium.")
        #8
        formatted_date_time = current_date_time.strftime("%a %b %d %H:%M:%S %Y")
        print(formatted_date_time)


    except FileNotFoundError as file_not_found_error: #9
        print(f"Error: missing file {file_not_found_error}") #9


if __name__ == "__main__":
    main()