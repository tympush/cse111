import random

def main():

    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words = ["apple", "car", "join"]
    print(words)

    append_random_words(words)
    print(words)

    append_random_words(words, 3)
    print(words)

def append_random_numbers(numbers_list, quantity=1):

    for i in range(quantity):
        numbers_list.append(round(random.uniform(0,100), 1))

def append_random_words(words_list, quantity=1):

    random_words_list = ["apple", "car", "join", "love", "smile", "cloud", "head", "pan"]

    for i in range(quantity):
        words_list.append(random.choice(random_words_list))

if __name__ == "__main__":
    main()