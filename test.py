print()
secret_word = "pathway"
guesses = 0
while True:
    guess = input("Guess the secret word: ")
    guesses += 1
    if guess == secret_word:
        print("Congratulations! You guessed the secret word in", guesses, "guesses.")
        break
print()
secret_word = "pathway"
guesses = 0
while True:
    guess = input("Guess the secret word: ")
    guesses += 1
    if len(guess) != len(secret_word):
        print("Your guess should be", len(secret_word), "letters long. Try again.")
    else:
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += secret_word[i].upper()
            elif guess[i] in secret_word:
                hint += guess[i].lower()
            else:
                hint += ""
        print("Hint:", hint)
        if guess == secret_word:
            print("Congratulations! You guessed the secret word in", guesses, "guesses.")
            break