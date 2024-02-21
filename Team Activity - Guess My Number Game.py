import random

playingLoop = True

while playingLoop == True:
    magicNumber = random.randint(1,100)
    numberOfGuessed = 1

    guess = int(input("What is your guess? "))

    while guess != magicNumber:
        numberOfGuessed = numberOfGuessed + 1

        if guess < magicNumber:
            print("Higher")
            guess = int(input("What is your guess? "))
        elif guess > magicNumber:
            print("Lower")
            guess = int(input("What is your guess? "))

    print("You guessed it!")
    print(f"Your number of guesses was {numberOfGuessed}")

    playQuestion = input("Do you want to play again? ")
    if playQuestion.lower() != "yes":
        playingLoop = False