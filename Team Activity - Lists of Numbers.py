numbersList = []
numberTotal = 0
largestNumber = 0
smallestNumber = 1000000

while 1 == 1:
    numberInput = int(input("Enter number: "))

    if numberInput == 0:
        break

    numbersList.append(numberInput)

for i in numbersList:
    numberTotal += i
print(f"The sum is: {numberTotal}")

numberAverage = numberTotal / len(numbersList)
print(f"The average is: {numberAverage}")

for i in numbersList:
    if largestNumber < i:
        largestNumber = i
print(f"The largest number is: {largestNumber}")

for i in numbersList:
    if smallestNumber > i and i >= 0:
        smallestNumber = i
print(f"The smallest positive number is: {smallestNumber}")

numbersList.sort()
for i in numbersList:
    print(i)