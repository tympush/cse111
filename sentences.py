# Exceeding the Requirements:
# added more parts to the sentences: second preposition, adjectives, random punctioation
# changed prepositions to use a local randomised quanity so that they are not locked to using the same quantity as the main noun

# IMPORTANT!
# the rubric requires me to have a parameter in the get_prepositional_phrase function
# i changed this in making my second alteration to the program
# the original versions of the function and the sentance assembler with this requirement are commented out

import random

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word

def get_verb(quantity, tense):

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    word = random.choice(words)
    return word

def get_preposition():

    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    word = random.choice(words)
    return word

#def get_prepositional_phrase(quantity):
#
#    quantity = random.randint(1,2)
#
#    phrase = (f"{get_preposition()} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}")
#    return phrase

def get_prepositional_phrase():

    quantity = random.randint(1,2)

    phrase = (f"{get_preposition()} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}")
    return phrase

def get_punctiation():

    words = [".", "?", "!"]

    word = random.choice(words)
    return word

def get_adjective():

    words = ["happy", "sad", "tired", "nervous", "relaxed", 
        "shy", "brave", "timid", "playful", "noisy", 
        "quiet", "bright", "dark", "colorful", "mysterious", 
        "gentle", "fearful", "careful", "careless", "grumpy"]
    
    word = random.choice(words)
    return word



def make_sentence(quantity, tense):

    sentence = (f"{get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase()} {get_prepositional_phrase()}{get_punctiation()}")
#    sentence = (f"{get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)} {get_prepositional_phrase(quantity)}{get_punctiation()}")
    return sentence

def main():

    print(f"{make_sentence(1,'past')}")
    print(f"{make_sentence(1, 'present')}")
    print(f"{make_sentence(1,'future')}")
    print(f"{make_sentence(2,'past')}")
    print(f"{make_sentence(2,'present')}")
    print(f"{make_sentence(2,'future')}")



main()