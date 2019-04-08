from random import randint


def game():

    selection = input("Enter your selection: ")
    oposition_num = randint(1, 3)
    oponent_selection = ""
    result = ""
    win_count = 0
    cpu_count = 0

    if oposition_num == 1:
        oponent_selection = "rock"

    elif oposition_num == 2:
        oponent_selection = "paper"

    elif oposition_num == 3:
        oponent_selection = "scisors"

    if selection == "rock" and oponent_selection == "paper":
        result = "You Lose"

    elif selection == "rock" and oponent_selection == "scisors":
        result = "You Win"

    elif selection == "rock" and oponent_selection == "rock":
        result = "Draw"

    elif selection == "paper" and oponent_selection == "rock":
        result = "You Win"

    elif selection == "paper" and oponent_selection == "scisors":
        result = "You Lose"

    elif selection == "paper" and oponent_selection == "paper":
        result = "Draw"

    elif selection == "scisors" and oponent_selection == "rock":
        result = "You Lose"

    elif selection == "scisors" and oponent_selection == "paper":
        result = "You Win"

    elif selection == "scisors" and oponent_selection == "scisors":
        result = "Draw"

    if result == "You Win":
        win_count = win_count + 1

    elif result == "You Lose":
        cpu_count = cpu_count + 1

    print("CPU selects " + oponent_selection)
    print(result)
    print("\nScore: Player " + str(win_count) + " CPU " + str(cpu_count) + "\n")


while True:
    answer = input("do you want to play?: ")
    if answer == 'y':
        game()
    elif answer == 'n':
        break
    else:
        print("dont understand")