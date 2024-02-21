import csv

def read_dictionary(filename):

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[0]
                dictionary[key] = row_list
    
    return dictionary

def main():

    student_list = read_dictionary("students.csv")

    id_input = input("Please enter an I-Number (xxxxxxxxx): ")

    if id_input in student_list:
        print(student_list[id_input][1])
    else:
        print("No such student")

if __name__ == "__main__":
    main()