print("This program is an implementation of the Rosenberg\nSelf-Esteem Scale. This program will show you ten\nstatements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the\nstatements by responding with one of these four letters:\n")
print("D means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n")

def calculate_positive_answer(answer):

    if answer == "D":
        score = 0
    elif answer =="d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3

    return score

def calculate_negative_answer(answer):

    if answer == "D":
        score = 3
    elif answer =="d":
        score = 2
    elif answer == "a":
        score = 1
    elif answer == "A":
        score = 0

    return score

def main():

    score = 0

    score += calculate_positive_answer(input("I feel that I am a person of worth, at least on an equal plane with others.\nEnter D, d, a, or A: "))
    score += calculate_positive_answer(input("I feel that I have a number of good qualities.\nEnter D, d, a, or A: "))
    score += calculate_negative_answer(input("All in all, I am inclined to feel that I am a failure.\nEnter D, d, a, or A: "))
    score += calculate_positive_answer(input("I am able to do things as well as most other people.\nEnter D, d, a, or A: "))
    score += calculate_negative_answer(input("I feel I do not have much to be proud of.\nEnter D, d, a, or A: "))
    score += calculate_positive_answer(input("I take a positive attitude toward myself.\nEnter D, d, a, or A: "))
    score += calculate_positive_answer(input("On the whole, I am satisfied with myself.\nEnter D, d, a, or A: "))
    score += calculate_negative_answer(input("I wish I could have more respect for myself.\nEnter D, d, a, or A: "))
    score += calculate_negative_answer(input("I certainly feel useless at times.\nEnter D, d, a, or A: "))
    score += calculate_negative_answer(input("At times I think I am no good at all.\nEnter D, d, a, or A: "))

    print("For each of the following, please rate the extent to which you agree with each statement,\nusing the scale from 1 to 5 as shown below. Please respond as you really feel,\nrather than how you think “most people” feel.\n")
    print("1 means you strongly disagree with the statement.\n2 means you disagree with the statement.\n3 means you neither agree nor disagree.\n4 means you agree with the statement.\n5 means you strongly agree with the statement.\n")

    NRList = []

    NRList.append(float(input("My ideal vacation spot would be a remote, wilderness area.\nEnter 1, 2, 3, 4, 5: ")))
    NRList.append(float(input("I always think about how my actions affect the environment.\nEnter 1, 2, 3, 4, 5: ")))
    NRList.append(float(input("My connection to nature and the environment is a part of my spirituality.\nEnter 1, 2, 3, 4, 5: ")))
    NRList.append(float(input("I take notice of wildlife wherever I am.\nEnter 1, 2, 3, 4, 5: ")))
    NRList.append(float(input("My relationship to nature is an important part of who I am.\nEnter 1, 2, 3, 4, 5: ")))
    NRList.append(float(input("I feel very connected to all living things and the earth.\nEnter 1, 2, 3, 4, 5: ")))

    NRAverage = sum(NRList) / len(NRList)

    print(f"Your score is {score}.\nA score below 15 may indicate problematic low self-esteem.\nYour NR-6 score is {NRAverage}.")
    
main()