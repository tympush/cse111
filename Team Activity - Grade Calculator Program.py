percentageGrade = float(input("What is you percetage grade? "))

if(percentageGrade >= 90):
    letter = "A"
elif(percentageGrade >= 80):
    letter = "B"
elif(percentageGrade >= 70):
    letter = "C"
elif(percentageGrade >= 60):
    letter = "D"
else:
    letter = "F"

remain = percentageGrade % 10
#print(remain)

if remain >= 7 and letter != "A" and letter != "F":
    bonus = "+"
elif remain < 3 and letter != "F":
    bonus = "-"
else:
    bonus = ""

print(f"Your grade is {letter}{bonus}.")

if(percentageGrade >= 70):
    print("You have passed the course.")
else:
    print("You have not passed the course, better luck next time.")