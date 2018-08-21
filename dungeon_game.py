import random
import os
import sys


#pick random location player

#pick random location exit door

#pick random location monster

#draw player in grid

#take input for movement

#move player unless invalid move

#check for win loss

#clear screen and redraw grid

CELLS = [(0, 0), (1, 0), (2, 0),(3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
         ]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "left":
        x -= 1
    if move == "right":
        x += 1
    if move == "up":
        y -= 1
    if move == "down":
        y += 1
    return x, y


def get_moves(player):
    moves = ["left", "right", "up", "down"]
    x, y = player
    if y == 0:
        moves.remove("up")
    if y == 4:
        moves.remove("down")
    if x == 0:
        moves.remove("left")
    if x == 4:
        moves.remove("right")
    return moves
def draw_map(player):
    print("_ " * 5)
    tile = "|{}"
    for cell in CELLS:
        x,y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def play_again():
    retry =input("Do you want to try again [Y/N]")
    if retry.upper() == "Y":
        game_loop()
    elif retry.upper() == "N":
        sys.exit()
    else:
        print("invalid answer")
        play_again()

def game_loop():
    monster, door, player = get_locations()

    while True:
        clear_screen()
        valid_moves = get_moves(player)
        draw_map(player)
        print("you're currently in room {}".format(player))  # Fill with player postition
        print("You can move {}".format(", ".join(valid_moves)))  # fill with available moves
        print("Enter Q to QUIT")
        move = input("> ")
        if move.upper() == "Q":
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                print("AAAW, you hit the monster, game over :(\n")
                play_again()
            if player == door:
                print("Congratulations, you've won <3\n")
                play_again()
        else:
            input("\n ** Walls are hard, don't move into them** \n")



clear_screen()
print("Welcome to the Dungeon!")
input("press return to start")
clear_screen()
game_loop()
