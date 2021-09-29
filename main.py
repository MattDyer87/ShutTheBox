"""
The game Shut the Box!
"""
import random

print("Welcome to Shut the Box!")

game_board = [1,2,3,4,5,6,7,8,9]

playing = True

print("GameBoard:", "|".join(f"{t}" for t in game_board))

def roll():
    roll = random.randint(1, 6)
    return roll

def update_game_board(tab):
    if tab != None:
        game_board[tab-1] = "*"
        

while playing:
    first_die = roll()
    second_die = roll()
    print("Current Roll:", first_die, second_die)

    remaining = list(i for i in game_board if isinstance(i, int))
    # for i, number in enumerate(remaining[:-1]):
    #         complementary = first_die + second_die - number
    #         if complementary in remaining[i+1:]:
    #             choosing = True
    #         else:
    #             print("Bummer! Game Over!")
    #             print("Your Score:", sum(remaining))
    #             choosing = False
    #             playing = False
    #             break
    choosing = True

    while choosing:

        choices = input("Enter the tabs you wish to flip separated by a space (q to quit)")
        if choices[0].lower() == "q":
            print("Thanks for playing!")
            print("Your Score:", sum(remaining))
            playing = False
            choosing = False
            break

        if len(choices) > 3:
            print("You must choose only 1 or 2 numbers")
            continue

        if len(choices) > 1:
            choice1, choice2 = list(map(int, choices.split()))
        else:
            choice1 = choices[0]
            choice2 = None
        
        if not isinstance(choice1, int) or not isinstance(choice2, int):
            print("Your selections must be numbers from 1-9 or 'q' to quit")
            continue

        if choice1 + choice2 != first_die + second_die:
            print("You must choose 2 that add up to your combined dice roll")
            continue

        if game_board[choice1-1] == "*" or game_board[choice2-1] == "*":
            print("That has already been used")
            continue

        choosing = False
            
    update_game_board(choice1)
    update_game_board(choice2)
    print("GameBoard:", "|".join(f"{t}" for t in game_board))


    

    remaining = list(i for i in game_board if isinstance(i, int))

    

    if remaining == 0:
        print("Congratulations! You Shut the Box!")
        break


