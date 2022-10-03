import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_draw = (random.sample((cards), 2))
computer_draw = (random.sample((cards), 2))

player_list = player_draw
computer_list = computer_draw

player_list = list(map(int, player_list))
computer_list = list(map(int, computer_list))

player_score = player_list[0] + player_list[1]
computer_score = computer_list[0] + computer_list[1]

player_score = int(player_score)
computer_score = int(computer_score)

game_finish = False
while not game_finish:

    print(player_list)
    print(computer_list)

    if player_score > 21:
        if 11 in player_list:
            player_score -= 10
            player_list[player_list.index(11)] = 1

            if player_score > 21:
                print("User lost")
                game_finish = True

    if player_score == 21:
        print("User Won")
        game_finish = True

    if computer_score == 21:
        print("User Lost")
        game_finish = True

    if computer_score > 21:
        print("User won")
        game_finish = True

    if player_score < 21:
        player_choice = input("Do you want to draw? *yes* *no*")

        if player_choice == "yes":
            player_list.append((random.choice((cards))))
            player_score = sum(player_list)
        if computer_score < 17:
            computer_list.append((random.choice((cards))))
            computer_score = sum(computer_list)
        elif player_choice == "no":

            if computer_score < 17:
                computer_list.append((random.choice((cards))))
                computer_score = sum(computer_list)

            if player_score > computer_score:
                print("User won")

                game_finish = True
            else:
                print("User lost")

                game_finish = True
