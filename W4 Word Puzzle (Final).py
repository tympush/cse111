#creativity:
#I made a list with 30 food items that the secret word is randomly chosen from
#I also made the game check if the user inputted something other than letters using isalpha
#Lastly, the game will give you a rank based on how many guesses you've had

import random

secretWordList = ["apple","banana","carrot","grape","cheese","bread","potato","melon","pepper","tomato","onion","lemon","peanut","yogurt","cherry","pizza","salad","muffin","cookie","orange","honey","toast","cereal","shrimp","pasta","steak","chicken","burger","salmon","sushi"]
secretWord = random.choice(secretWordList)
gameLoop = True

#set the hint to _ for each of the characters in the secret word for the first hint
hint = ""
for i in secretWord:
    hint += "_"

print(f"Your hint is: {hint}")
guess = input("What is your guess? ")
numberOfGuesses = 1

while gameLoop == True:

    if not guess.isalpha():
        print("Sorry, the guess must only contain letters.\n")

        #resets the guess to the letter q to be able to pass the check again
        #but give you an empty hint because none of the words have the letter q
        #(i would have to generate a random string of letters that do not appear in the secret word if all letters were used, but this is an easier solution for now)
        guess = ""
        for i in secretWord:
            guess += "q"

    elif len(secretWord) != len(guess):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")

        #also resets the guess to q
        guess = ""
        for i in secretWord:
            guess += "q"

    elif secretWord == guess.lower():
        gameLoop = False

    else:
        hint = ""
        for index in range(len(guess)):
            if guess[index].lower() == secretWord[index]:
                hint += guess[index].upper()
            elif guess[index].lower() in secretWord:
                hint += guess[index].lower()
            else:
                hint += "_"

        previousGuess = guess
        
        print(f"Your hint is: {hint}")
        guess = input("What is your guess? ")
        numberOfGuesses = numberOfGuesses + 1


print("Congratulations! You guessed it!")
print(f"It took you {numberOfGuesses} guesses.")

if numberOfGuesses < 4:
    print("Your rank is: A")
elif numberOfGuesses < 8:
    print("Your rank is: B")
elif numberOfGuesses < 16:
    print("Your rank is: C")
elif numberOfGuesses < 32:
    print("Your rank is: D")
else:
    print("Your rank is: F")
