#I added a couple more words, inserted some randomised elements into the story, and added a continuation to the story with a random outcome.
#I also maybe the game loop and ask whether you want to play again

import random

#lists for some of the randomised parts
troubleScaleList = ["trouble","big trouble","really big trouble","huge trouble","a bit of trouble","quite a pickle","quite a sticky situation"]
opinionList = ["I had to do something.","I had to stop this.","This was outrageous!","I found this unacceptable."]
vowelList = ["a","e","i","o","u","y"]
outcomeList = ["The beast saw me comming, quickly turned around and ate me, then my family.","I tripped and fell down.","The beast turned around, saw me, and quickly ran away scared.","I took my swing, hit the beast right on the head and it ran away.","I attacked, and battled the beast. After a long and exhausting fight, I won.","The beast saw me, it couldn't handle my pure awesomeness, and melter right before my eyes."]

#the loop
loopGame = True
while(loopGame == True):
    
    #picking the random outcomes from the lists
    troubleScale = random.choice(troubleScaleList)
    opinion = random.choice(opinionList)

    #questions for the user
    print("Please enter the following:\n")
    time = input("time (when?): ")
    advective = input("adjective: ")
    animal = input("animal: ")
    verb = input("verb: ")
    exclamation = input("exclamation: ")
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    weaponObject = input("object: ")

    #checking for the first letter of the weapon object to descide whether "a" or "an" should be used
    #(I'm sure there is a more efficient way of doing this, but this is what I came up with)
    weaponLetter = weaponObject.lower()[0]
    if(weaponLetter in vowelList):
        weaponPreset = "an"
    else:
        weaponPreset = "a"

    #the main part of the story
    print(f'\nYour story is:\n\n{time.capitalize()}, I was in {troubleScale}. It all started when I saw a very {advective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family. {opinion} I grabbed {weaponPreset} {weaponObject.lower()} and rushed towards the creature.')

    #askin the player to roll a dice to determine the outcome of the story
    input("\nRoll a dice to determine the outcome (Press Enter)")
    diceRoll = random.randint(1,6)
    print(f"You rolled: {diceRoll}\n")

    print(outcomeList[diceRoll-1])

    if(diceRoll == 1 or diceRoll == 2):
        print("I couldn't save my family. I failed.\n")
    elif(diceRoll == 3):
        print("I guess I saved my family?\n")
    else:
        print("I saved my family! I was a true hero.\n")

    #loop that asks player whether they want to play again
    questionLoop = True
    while(questionLoop == True):
        answer = input("Do you want to play again? (yes/no): ")
        if(answer.lower() == "yes"):
            questionLoop = False
            print("\n")
        elif(answer.lower() == "no"):
            questionLoop = False
            loopGame = False
        else:
            print("Incorrect Input, try again.")

#final message if they said no
print("\nThanks for playing!")