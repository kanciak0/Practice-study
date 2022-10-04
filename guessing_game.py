import random

correct_answer = random.randint(1, 100)
Game_difficulty = str(input("Choose game difficulty: Type *hard* or *normal*"))


def game_hard():
    finished = False
    counter = 5
    user_choice = int(input("Choose number from 1 to 100"))
    while not finished:
        if user_choice > correct_answer:
            print("The number is too high,try once again")
            counter -= 1
            print(f"Amount of tries:{counter}")
            user_choice = int(input("Choose number from 1 to 100"))

        elif user_choice < correct_answer:
            print("The number is too low, try once again")
            counter -= 1
            print(f"Amount of tries:{counter}")
            user_choice = int(input("Choose number from 1 to 100"))

        if user_choice == correct_answer:
            print(" Game is over you won")
            finished = True

        if counter == 0:
            print("Game is over you lost")
            finished = True


def game_normal():
    finished = False
    counter = 10

    while not finished:
        user_choice = int(input("Choose number from 1 to 100"))
        if user_choice > correct_answer:
            print("The number is too high,try once again")
            counter -= 1
            print(f"Amount of tries:{counter}")

        if user_choice < correct_answer:
            print("The number is too low, try once again")
            counter -= 1
            print(f"Amount of tries:{counter}")

        if user_choice == correct_answer:
            print("Game is over you won")
            finished = True

        if counter == 0:
            print("Game is over you lost")
            finished = True


if Game_difficulty == "hard":
    game_hard()

elif Game_difficulty == "normal":
    game_normal()
