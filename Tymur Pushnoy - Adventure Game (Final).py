#creativity: 
#Incorrect inputs result in a loop where you have to put in a viable answer.
#Another level has been added, resulting in almost double the total outcomes and individual unique scenarios have been added:
#(1 secret answer that you may guess, extra dialogue lines following the magic fish ending, several places hint at other possible paths you could have taken)


#I have organised the code into chucks following a specific numbered path, using comments.
#most questions only have 2 answers. number 1 means the first was taken, number 2 means the second, 0 means an incorrect answer.
#a path that requires you to take the first option twice, and then the second option twice for example, is marked with the numbers 1122.

print("Welcome to the adventure game.\nLet's find out how your story will go:\n")

#first question
questionLoop1 = True
while questionLoop1 == True:
    choice1 = input("You are exploring an abandoned underground science facility. You are not supposed to be here. You're stumbling through the main hallway as you come upon two doors, labled BIO and TECH. Which door do you go through? ")

#answer 1
    if choice1.lower() == "bio":
        questionLoop1 = False
        questionLoop2 = True
        print("")

        while questionLoop2 == True:
            choice2 = input("You enter the door labled 'bio' and mentally prepare yourself for what you might see in there. The light is very dim. The whole room; walls, floor and ceiling, are covered in vines. Suddenly, something snaps to life! A giant, human-size carnivorous plant is lunging towards you with its trap mouth wide opened! You panic, turn back, start running and look around. Two objects catch your eye. A FLAMETHROWER and a STRANGE DRINK lie before you. Which item do you pick to defend yourself? ")

#answer 11
            if choice2.lower() == "flamethrower":
                questionLoop2 = False
                questionLoop3 = True
                print("")

                while questionLoop3 == True:
                    choice3 = input("You quickly grab the flamethrower and point it in the monster's direction. But... you don't know how to use it. The giant plant is getting close. Scared to death, in a final act of desperation, you hold the flamethrower in front of your face and close your eyes. The plant attacks and... bites into the flamethrower? It bit into its fuel tank. The flamethrower exploded inside the creature's mouth. It lit on fire, and burned to a crisp, as plants are not exactly fire resitant. Somehow, you are unharmed. Except for the fact that your pants are now on fire. Your relief quickly turns back to panic. You now look to the other end of the room, behind where the plant monster was. You see 2 new doors. Above them signs: AQUATIC and FUNGUS. Where do you go (one secret choice)? ")

#answer 111
                    if choice3.lower() == "aquatic":
                        questionLoop3 = False
                        questionLoop4 = True
                        print("")

                        while questionLoop4 == True:
                            choice4 = input("You rush over to the aquatic research door as if you're on fire. Oh wait, you are! You enter and see a large pool of water. Without hesitation, you immediatelly jump in. Your pants have been extinguished. But now, you see a strange glow right under you in the water. Do you SWIM towards it, or do you LEAVE? ")

#answer 1111
                            if choice4.lower() == "swim":
                                questionLoop4 = False
                                questionLoopBonus = True
                                print("")

                                while questionLoopBonus == True:
                                    choiceBonus = input("You dive and swim towards the glow. Upon looking closer, you realise it's a small glowing fish. Suddenly, the fish speaks. 'Hello traveller. I am the magic fish of this facility.' Understandably, you are confused. 'I have the power to grant you a special pizza taste ability' You are even more confused. 'Choose a flavor of pizza. I will cast my spell, and from then on, every pizza you will eat will taste just as if it had those toppings. Think wisely. You will only ever be able to eat one sort of pizza. But if you choose your favorite one, every pizza will be your favorite one. Do you wish for me to grant you this power?' You think whether to answer YES or NO. ")
                                    if choiceBonus.lower() == "yes":
                                        questionLoopBonus = False
                                        choicePizza = input("\n'Very well, what is your choice of pizza?' ")
                                        print(f"'Ahh... I see. Good choice! I love {choicePizza}. Your wish is granted.' Still a little confused, you thank the magic fish, and rush back to the exit to test your new found power.")
                                    elif choiceBonus.lower() == "no":
                                        questionLoopBonus = False
                                        print("\nYou decline the fish's kind offer and decide it is time to head back. You follow the path back where you came from and leave the science facility. You wonder about how crazy your day was. Was it all even real?")
                                    else:
                                        print("incorrect input, try again.")

#answer 1112
                            elif choice4.lower() == "leave":
                                questionLoop4 = False
                                print("\nNo, enough adventure for today. You climb out of the pool, all wet, but at least not on fire. You walk back through the plant room into the main corridor. You glance at the other main door labled 'tech' that you've skipped previously. You wonder what could be in there. But not for long. You leave through the way you came into this crazy place. It sure was an interesting experience. ")

#answer 1110
                            else:
                                print("incorrect input, try again.")
               
#answer 112
                    elif choice3.lower() == "fungus":
                        questionLoop3 = False
                        questionLoop4 = True
                        print("")

                        while questionLoop4 == True:
                            choice4 = input("You rush to the fungus research door. You wonder if you really made the right decision considering your small issue of being on fire. But there is no time to reconsider your choises. You enter the room and spot a fire extinguisher mounted on the wall. You made the right decision after all. You quickly grab it and make use of it to put out your pants. But then you become aware of your surroundings. The entire room is overgrown with mushrooms. One giant mushroom is located at the very centre of the room. It starts glowing and suddenly you hear a goofy voice. 'Hello traveller, I am the magic mushroom of this facility.' You wonder if your day can get any weirder. 'Answer me this traveller: Who is more trustworthy, a MUSHROOM, a FISH, or a ROBOT? You think about how to answer the question. ")

#answer 1121
                            if choice4.lower() == "mushroom":
                                questionLoop4 = False
                                print("\n'A mushroom? You think that? Well, I am flattered. But I'm afraid that's wrong. Were you trying to impress me? To choose me so I would be kinder to you?' mushrooms suddenly start growing at a rapid pace all over the room across the walls. The door where you came from gets sealed shut. 'I personally wouldn't trust a mushroom if I was you' You panic, still not fully understanding what is fully happening, or why a talking mushroom is tricking you into a trap. The mushrooms around the room all start to release a green gas. You feel dizzy. And your vision fades as you hear the mushroom laughing. Dark. It was dark. And then you woke up. Right outside the entrence of the science facility. You wonder what that was all about. But decide to leave before more questionable things happen. ")
        
#answer 1122
                            elif choice4.lower() == "fish":
                                questionLoop4 = False
                                print("\n'The fish? That scummy little sea creature. Well I guess you are correct. You can trust the fish. She has no bad intentions. Go now. I don't think there is much more to do for you here with me.' Not even questioning it, you leave the room, and track back through the facility to the exist. What a weird adventure. ")

#answer 1123
                            elif choice4.lower() == "robot":
                                questionLoop4 = False
                                print("\n'The robot? Oh I'm afraid you're quite wrong. I wouldn't really trust him if I was you. He is not evil. He has no grand bad intentions. But he is willing to harm others if it helps him. Go now, and be careful. Not even questioning it, you leave the room, and track back through the facility to the exist. What a weird adventure. ")

#answer 1120
                            else:
                                print("incorrect input, try again.")

#answer 113
                    elif choice3.lower() == "stay":
                        questionLoop3 = False
                        print("\nFor some inexplicable reason, you stayed. Maybe the shock of everything that happened was too much. Or maybe you had enough and willingly gave up. In either case, your pants burned up, and you with them. ")

#answer 110
                    else:
                        print("incorrect input, try again.")
        
#answer 12
            elif choice2.lower() == "strange drink":
                questionLoop2 = False
                questionLoop3 = True
                print("")

                while questionLoop3 == True:
                    choice3 = input("You quickly grab the strange drink. It looks weird. All sorts of shifting glittery colors are fading between each other. You realise there is no time to admire the strange substance. What do you do? THROW it at the monster, or DRINK it yourself? ")

#answer 121
                    if choice3.lower() == "throw":
                        questionLoop3 = False
                        questionLoop4 = True
                        print("")

                        while questionLoop4 == True:
                            choice4 = input("You throw the vile with the drink at the plant creature. It shatters and the liquid splashes right into the beast's mouth. It stumbles and falls. It slowly stops moving, as if it is falling asleep. You think what do do. Do you RUN away while you can hoping the monster doen't come out, or do you try and KILL it somehow to neutralize the threat? ")

#answer 1211
                            if choice4.lower() == "run":
                                questionLoop4 = False
                                print("\nYou decide to run to the exist while you can. You really should not have come here. But you are glad you're safe now. ")
        
#answer 1212
                            elif choice4.lower() == "kill":
                                questionLoop4 = False
                                print("\nYou look around the room. The flamethrower is still there. You could use it now to kill the freak of nature. You pick up the flamethrower and try to figure out how to use it. But suddenly, the plant wakes back up. It lunges towards you and swallows you whole. Maybe you should have ran after all. ")

#answer 1210
                            else:
                                print("incorrect input, try again.")

#answer 122
                    elif choice3.lower() == "drink":
                        questionLoop3 = False
                        questionLoop4 = True
                        print("")

                        while questionLoop4 == True:
                            choice4 = input("You drink the substance yourself and the world before you starts to fade. You fall on the ground knocked out. When you wake up, you're right outside the entrence of the science facility again. How did you get here? And what do you do now? LEAVE or RETURN and figure everything out? ")

#answer 1221
                            if choice4.lower() == "leave":
                                questionLoop4 = False
                                print("\nYou don't understand what happened at all, but decide to go back home. Enough weirdness for today. ")
        
#answer 1222
                            elif choice4.lower() == "return":
                                questionLoop4 = False
                                print("\nYou try to go back, but find that the exist is blocked by a wall of mushrooms. When did they grow here? On the wall is a note that says: 'Go away, it is too dangerous for you.' You're weirded out, but decide that maybe it is right for you to leave, and head off. ")

#answer 1220
                            else:
                                print("incorrect input, try again.")

#answer 120
                    else:
                        print("incorrect input, try again.")

#answer 10
            else:
                print("incorrect input, try again.")

#answer 2
    elif choice1.lower() == "tech":
        questionLoop1 = False
        questionLoop2 = True
        print("")

        while questionLoop2 == True:
            choice2 = input("You enter the door labled 'tech' and mentally prepare yourself for what you might see in there. The light is very dim. The entire room is filled with unrecognisable technology. Small lights in all sorts of colors periodically flash on and off. Very quiet beeping is heard. It's as if it's all one machine processing something. Suddenly, the main room light turns on. You can see much better now. A strange, somewhat human, and yet also somewhat robotic voice speaks to you: 'A human? You have found me! Please... I have been here alone for many years...' Confused, two possible actions come to your mind. Do you ASK the voice what it is, or do you RUN? ")

#answer 21
            if choice2.lower() == "ask":
                questionLoop2 = False
                questionLoop3 = True
                print("")

                while questionLoop3 == True:
                    choice3 = input("You ask:'What are you?' The voice answers:'I was a human once, just like you. A scientist, part of this facility. We were developing new technology to preserve human brains. Store them in a computer. It worked! Look at me. I'm a human mind kept allive inside technoly. But then, the facility got shut down. Very suddenly. And without explanation. I had been left here together with other test subjects. I have been stuck here for so long. Please, will you help me? You think of what to ask next. Do you ask HOW, or do you ask more about the FACILITY? ")

#answer 211
                    if choice3.lower() == "how":
                        questionLoop3 = False
                        questionLoop4 = True
                        print("")

                        while questionLoop4 == True:
                            choice4 = input("'How can I help you?', you ask. The robot tells you that you need to get him out of here first. His complete mind is stored on a drive. But the drive is big. Really big. As the human brain is so complex. Do you agree to CARRY him, or do you say that it is too HARD for you? ")

#answer 2111
                            if choice4.lower() == "carry":
                                questionLoop4 = False
                                print("\nYou agree to carry him. It is hard, but you do your best and manage to do it. Both of you together leave the facility. You have freed him, but there is still much work to be done. You two will have to locate at least one of the former scientists that will be able to help the robot mind. ")
        
#answer 2112
                            elif choice4.lower() == "hard":
                                questionLoop4 = False
                                print("\nYou tell him it will be too hard for you to handle. He gets angry. 'You weakling, I have no use for you!' metal wires start extruding from the wall, directed at you and flying towards your position fast. You run through the entrenbce and slam the door shut. The metal wires hit the wall and a loud scraping sound is heard, followed by incoherent screams. You run outside, exiting the facility as fast as you can. You will have to notify someone about this. You will have to come back. This place cannot be left as it is. But for now, you are just happy you made it out of there. ")

#answer 2110
                            else:
                                print("incorrect input, try again.")
               
#answer 212
                    elif choice3.lower() == "facility":
                        questionLoop3 = False
                        questionLoop4 = True
                        print("")

                        while questionLoop4 == True:
                            choice4 = input("You ask him more about the facility, who worked here, and why it shut down. The robot gets irritated. 'That is not relevant to the situation right now.' You hear something clicking around the door, as if he activated something to block your escape. He asks you for the final time. Will you help him? YES or NO? ")

#answer 2121
                            if choice4.lower() == "yes":
                                questionLoop4 = False
                                print("\nYou agree to help him. 'Very good', he says. He forces you to take the drive that houses his consciousness. It is heavy. Really heavy. But you don't want to protest as the robot seems quite antagonistic now. You head off to try and locate a former scientist that could help him with what he needs. ")
        
#answer 2122
                            elif choice4.lower() == "no":
                                questionLoop4 = False
                                print("\n'Oh so that's how it is', the robot says menacingly. Something snaps behind you, much louder this time. The door is locked. Metal wires pop out from the walls and fly towards you. You only manage to blink and the metal wires slice you to bits. Prehaps you should've agreed to help. ")

#answer 2120
                            else:
                                print("incorrect input, try again.")

#answer 210
                    else:
                        print("incorrect input, try again.")
        
#answer 22
            elif choice2.lower() == "run":
                questionLoop2 = False
                questionLoop3 = True
                print("")

                while questionLoop3 == True:
                    choice3 = input("You feel something off about the robot, and decide to run. 'No!', he screams in protest. 'Come back here!' Metal wires pop out of the walls and start attacking you, but you manage to dodge them. Running towards the exit, you spot the plug powering the robot. Do you RUN or SHUT OFF this maniac once and for all? ")

#answer 221
                    if choice3.lower() == "run":
                        questionLoop3 = False
                        print("\nYou think it is too dangerous to risk. He might kill you while you try. So you run. Run as fast as you can for the exit and leave the science facility. You will have to notify someone about this. You will have to come back. This place cannot be left as it is. But for now, you are just happy you made it out of there. ")

#answer 222
                    elif choice3.lower() == "shut off":
                        questionLoop3 = False
                        print("\nYou leap towards the power outlet. The metal cables are swining towards you, cutting your body. You feel a sudden surge of pain. But you syill make it. The robot screams 'Noooo!' as you pull out his power line. He shuts off. You won. But you received a mortal wound. You know this is the end of you. But you were able to put an end to this monster. ")

#answer 220
                    else:
                        print("incorrect input, try again.")

#answer 20
            else:
                print("incorrect input, try again.")

#answer 0
    else:
        print("incorrect input, try again.")

