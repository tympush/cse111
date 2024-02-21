import csv
import random


repeat_program = True


def get_data(file_name):
    user_data = {}

    with open(file_name, "rt") as csv_file:
        reader = csv.reader(csv_file)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[0]
                user_data[key] = row_list

    return user_data


def roll_dice(minimum, maximum):
    number = random.randint(minimum, maximum)
    return number


def play_game(username, data_dict):
    while True:
        try:
            dice_roll_amount = int(input("\nInput the number of dice to throw (1-100): "))
            if 1 <= dice_roll_amount <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    score_sum = 0
    for _ in range(dice_roll_amount):
        score_sum += roll_dice(1, 6)

    print(f"Your score: {score_sum}")

    if username in data_dict:
        data_dict[username][1] = str(int(data_dict[username][1]) + score_sum)
        data_dict[username][3] = str(int(data_dict[username][3]) + dice_roll_amount)
        data_dict[username][2] = str(round(int(data_dict[username][1]) / int(data_dict[username][3]), 2))
    else:
        data_dict[username] = [username, str(score_sum), str(round(score_sum / dice_roll_amount, 2)), str(dice_roll_amount)]

    write_data_to_csv(data_dict)

    print()

    return continue_input()


def write_data_to_csv(data_dict):
    with open("score.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        for user, data in data_dict.items():
            csv_writer.writerow(data)


def display_leaderboard(data_dict, option):
    if option == "1":
        sorted_users = sorted(data_dict.items(), key=lambda x: int(x[1][1]), reverse=True)[:10]
        print("\nTop 10 Users with Highest Total Score:")
        for user, data in sorted_users:
            print(f"{user} - {data[1]}")
    elif option == "2":
        sorted_users = sorted(data_dict.items(), key=lambda x: int(x[1][3]), reverse=True)[:10]
        print("\nTop 10 Users with Most Dice Thrown:")
        for user, data in sorted_users:
            print(f"{user} - {data[3]}")
    elif option == "3":
        sorted_users = sorted(data_dict.items(), key=lambda x: float(x[1][2]), reverse=True)[:10]
        print("\nTop 10 Users with the Best Luck")
        for user, data in sorted_users:
            print(f"{user} - {data[2]}")
    print()

    return continue_input()


def display_user_statistics(username, data_dict):
    if username in data_dict:
        print(
            f"\n{username}'s Statistics:\nTotal Score - {data_dict[username][1]}\nDice Thrown - {data_dict[username][3]}\nLuck - {data_dict[username][2]}\n"
        )
    else:
        print("\nNo user data exists.\n")

    return continue_input()


def shell(username):
    global repeat_program
    
    try:
        data_dict = get_data("score.csv")
    except FileNotFoundError:
        print("Error: File not found. Terminating program.")
        exit()

    print("\nOption 1 - Play\nOption 2 - Leaderboard\nOption 3 - User Statistics")
    action1 = input("Select an action (1/2/3): ")

    if action1 == "1":
        repeat_program = play_game(username, data_dict)

    elif action1 == "2":
        while True:
            print("\nOption 1 - Highest Total Score\nOption 2 - Most Dice Thrown\nOption 3 - Best Luck")
            action2 = input("Select a leaderboard option (1/2/3): ")
            if action2 in ["1", "2", "3"]:
                repeat_program = display_leaderboard(data_dict, action2)
                break

    elif action1 == "3":
        repeat_program = display_user_statistics(username, data_dict)


def continue_input():
    while True:
        user_input = input("Do you want to continue? (yes/no): ").lower()
        if user_input == "no":
            return False
        elif user_input == "yes":
            return True


def main():
    global repeat_program

    print("---------\nDice Game\n---------\n")
    username = input("Enter username: ")
    print(f"Welcome {username}")

    while repeat_program:
        shell(username)

    print("\nThank you for playing!")


if __name__ == "__main__":
    main()