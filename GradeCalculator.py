grade = input("What is your grade? ")
grade = int(grade)

if grade >= 90:
    print("Your grade is A.")
elif grade >= 80:
    print("Your grade is B.")
elif grade >= 70:
    print("Your grade is C.")
elif grade >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")

if grade >= 70:
    print("You have passed the course.")
else:
    print("You have not passed the course, better luck next time.")