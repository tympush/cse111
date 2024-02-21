secretWord = "hamburger"
numberOfGuesses = 0
guess = ""

while guess.lower() != secretWord:
    guess = input("What is your guess? ")
    numberOfGuesses = numberOfGuesses + 1

    if guess.lower() != secretWord:
        print("Your guess was not correct.")

print("Congratulations! You guessed it!")
print(f"It took you {numberOfGuesses} guesses.")