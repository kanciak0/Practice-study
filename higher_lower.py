from game_data import data
import random
import os
from time import sleep


def game():
    finished = False
    counter = 0
    while not finished:

        first_choice = random.choice(list(data))
        second_choice = random.choice(list(data))

        print(first_choice["name"])
        print(first_choice["description"])
        print(first_choice["country"])

        print("-------------------------------------------")

        print(second_choice["name"])
        print(second_choice["description"])
        print(second_choice["country"])

        a = str(input("Which one has more followers? Type 1 or 2"))

        if first_choice["follower_count"] > second_choice['follower_count'] and a == "1":
            counter += 1
            print(f"You won! Your score is: {counter}")

        elif second_choice["follower_count"] > first_choice['follower_count'] and a == "2":
            counter += 1
            print(f"You won! Your score is: {counter}")

        else:
            print(f"You lost! Try again! Your score was {counter}")
            finished = True
        sleep(1)
        os.system('cls')


game()
