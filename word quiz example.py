#set the secret word to pathway
#it has to be all lower case
secret_word = "pathway"

#game loop set to true, we will use this for the while loop
game_loop = True

#we set hint to an empty string
hint = ""
#then we add "_" to the hint for every character in the secret word
#so it will print the correct number of places for the hint
for i in secret_word:
    hint += "_"

#we print the hint we just made
print(f"Your hint is: {hint}")

#ask for the guess
guess = input("What is your guess? ")

#number of guesses starts at 1, because we just made the first guess
number_of_guesses = 1

#while loop continues while game_loop variable is set to true
while game_loop == True:

   #if statement cheks if the lenght of secret word is the same as the guess
   if len(secret_word) != len(guess):
      #if it's not the same lenght, it will say that is has to be the same lenght
      print("Sorry, the guess must have the same number of letters as the secret word.\n")

      #then it resets the guess to the correct lenght like we did with the hint at the start
      #this is so that we don't end up in this if statement again
      guess = ""
      for i in secret_word:
         guess += "_"

   #if the secret word and guess are the same, the loop is set to false, so the loop ends
   #the guess has to be set to lower case by .lower() because we want the guess to be correct even if it was capitalised
   elif secret_word == guess.lower():
      game_loop = False

   #else if the guess is not the wrong lenght and we have not guessed the word, the hint stuff will happen
   else:
      #the hint is reset to nothing
      hint = ""
      #then we repeat this for loop for every character in the guess
      for index in range(len(guess)):
         #if the letter from the guess and from the secret word are in the exact same place
         if guess[index].lower() == secret_word[index]:
            #that letter is added to the hint string as a capital letter
            hint += guess[index].upper()
         #if the letter is instead not in the right place but it is somewhere in the secret word
         elif guess[index].lower() in secret_word:
            #it is added to the hint string as a lower case letter
            hint += guess[index].lower()
         #otherwise just an empty _ is added
         else:
            hint += "_"
      
      #then we print the hint
      print(f"Your hint is: {hint}")

      #then we ask for the guess input again
      guess = input("What is your guess? ")
      #and we increase the number of guesses by 1
      number_of_guesses = number_of_guesses + 1

#when the loop is finished, we print these messages
print("Congratulations! You guessed it!")
print(f"It took you {number_of_guesses} guesses.")