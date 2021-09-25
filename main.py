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
    game_board[tab-1] = "*"
    print("GameBoard:", "|".join(f"{t}" for t in game_board))

while playing:
    first_die = roll()
    second_die = roll()
    print("Current Roll:", first_die, second_die)

    choices = input("Enter the tabs you wish to flip separated by a space (q to quit)")
    if choices.lower() == "q":
        print("Thanks for playing!")
        break
    if len(choices) > 1:
        choice1, choice2 = list(map(int, choices.split()))
    else:
        choice1 = choices
        choice2 = choices
    
    if game_board[choice1-1] == "*" or game_board[choice2-1] == "*":
        print("Your Score:", sum(remaining) )
        break
    
    if game_board[choice1-1] + game_board[choice2-1] != first_die + second_die:
        print("You must choose 2 that add up to your combined dice roll")
        break

    update_game_board(choice1)
    update_game_board(choice2)

    remaining = list(i for i in game_board if isinstance(i, int))
    
    if remaining == 0:
        print("Congratulations! You Shut the Box!")
        break


