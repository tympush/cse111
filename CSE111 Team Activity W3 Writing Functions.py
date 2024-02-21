from datetime import datetime


def main():
    gender = input("Gender (male/female): ")
    birth = input("Birth date (YYYY-MM-DD): ")


    weightUnit = input("Weight unit (pounds/stone): ")
    if weightUnit.lower() == "pounds":
        weight = float(input("Weight (U.S. pounds): "))
        weight_kg = kg_from_lb(weight)
    else:
        weight = float(input("Weight (British stones): "))
        weight_kg = kg_from_stone(weight)


    height = input("Height (feet'inches): ")

    age = compute_age(birth)

    height_cm = cm_from_in(height)

    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    print(f"{age}, {weight_kg:.2f}kg, {(height_cm/100):.2f}m, {bmi:.2f}, {bmr:.2f}")


def compute_age(birth_str):

    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):

    kg = pounds * 0.45359237

    return kg

def kg_from_stone(stone):

    kg = stone * 6.35029

    return kg


def cm_from_in(inches):

    splitList = inches.split("'")
    converted = float(splitList[0]) * 12 + float(splitList[1])
    cm = converted * 2.54

    return cm


def body_mass_index(weight, height):

    bmi = 10000 * weight / height ** 2

    return bmi


def basal_metabolic_rate(gender, weight, height, age):

    if gender.lower() == "female":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age

    return bmr


main()