import random

numberOfRolls = 10000
numberOfSuccess = 0

while numberOfRolls > 0:
    numberOfRolls = numberOfRolls - 1

    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    d5 = random.randint(1,6)
    d6 = random.randint(1,6)
    d7 = random.randint(1,6)
    d8 = random.randint(1,6)

    numberOf6 = 0

    if d1 == 6:
        numberOf6 = numberOf6 + 1
    if d2 == 6:
        numberOf6 = numberOf6 + 1
    if d3 == 6:
        numberOf6 = numberOf6 + 1
    if d4 == 6:
        numberOf6 = numberOf6 + 1
    if d5 == 6:
        numberOf6 = numberOf6 + 1
    if d6 == 6:
        numberOf6 = numberOf6 + 1
    if d7 == 6:
        numberOf6 = numberOf6 + 1
    if d8 == 6:
        numberOf6 = numberOf6 + 1

    if numberOf6 > 2:
        numberOfSuccess = numberOfSuccess + 1

print(numberOfSuccess)
