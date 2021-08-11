import random

# variable that holds the game board
# a dictionary that holds the possible actions (nums 1 - 9) and whether a player has made an action (X / O)
board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}


def print_board():
    print(f"{board[7]} | {board[8]} | {board[9]}\n"
          f"----------\n"
          f"{board[4]} | {board[5]} | {board[6]}\n"
          f"----------\n"
          f"{board[1]} | {board[2]} | {board[3]}\n")


def player_move():
    move = input("Your move?\n")

    try:
        move = int(move)
    except ValueError:
        print("Invalid action, type a number from 1 - 9")
    else:

        if move > 9 or move < 1:
            print("Invalid action, type a number from 1 - 9")
        else:

            for spot in board:
                if move == spot:
                    if board[spot] != " ":
                        print("Invalid action, that spot is already occupied, try another move")
                    else:
                        board[spot] = "X"


def enemy_move():
    cycle = True
    move = random.randint(1, 9)

    while cycle:
        for spot in board:
            if move == spot:
                if board[spot] != " ":
                    move = random.randint(1, 9)
                else:
                    board[spot] = "O"
                    cycle = False


def check_victory():
    # check rows
    if board[7] == "X" and board[8] == "X" and board[9] == "X":
        return True
    elif board[4] == "X" and board[5] == "X" and board[6] == "X":
        return True
    elif board[1] == "X" and board[2] == "X" and board[3] == "X":
        return True

    # check columns
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return True
    elif board[3] == "X" and board[6] == "X" and board[9] == "X":
        return True

    # check diagonals
    elif board[1] == "X" and board[5] == "X" and board[9] == "X":
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return True

    else:
        return False


def check_defeat():
    # check rows
    if board[7] == "O" and board[8] == "O" and board[9] == "O":
        return True
    elif board[4] == "O" and board[5] == "O" and board[6] == "O":
        return True
    elif board[1] == "O" and board[2] == "O" and board[3] == "O":
        return True

    # check columns
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return True
    elif board[3] == "O" and board[6] == "O" and board[9] == "O":
        return True

    # check diagonals
    elif board[1] == "O" and board[5] == "O" and board[9] == "O":
        return True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return True

    else:
        return False


def game():
    game_on = True
    print("Welcome to Tic Tac Toe")
    print("How to play: Type a number from 1 - 9 to make a move:")
    print(f"7 | 8 | 9\n"
          f"----------\n"
          f"4 | 5 | 6\n"
          f"----------\n"
          f"1 | 2 | 3\n")

    enemy_moves_counter = 0
    number_of_moves = 0

    while game_on:

        print_board()

        player_move()

        if check_victory():
            print_board()
            print(
                   f" _____.___.                      .__         ._.\n"
                    f"\__  |   | ____  __ __  __  _  _|__| ____   | |\n"
                     f"/   |   |/  _ \|  |  \ \ \/ \/ /  |/    \  | |\n"
                     f"\____   (  <_> )  |  /  \     /|  |   |  \  \|\n"
                     f"/ ______|\____/|____/    \/\_/ |__|___|  /  __\n"
                     f"\/                                     \/   \/\n")

            game_on = False

        number_of_moves += 1

        if enemy_moves_counter < 4:
            enemy_move()

            if check_defeat():
                print_board()
                print( f"_____.___.              .__                                ___\n" 
                       f"\__  |   | ____  __ __  |  |   ____  ______ ____    /\    /  / \n"
                        f"/   |   |/  _ \|  |  \ |  |  /  _ \/  ___// __ \   \/   /  /\n"  
                        f"\____   (  <_> )  |  / |  |_(  <_> )___ \\  ___/   /\  (  ( \n"  
                        f"/ ______|\____/|____/  |____/\____/____  >\___  >  \/   \  \ \n" 
                        f"\/                                     \/     \/         \__\ \n")

                print("Try again.")
                game_on = False

            enemy_moves_counter += 1
            number_of_moves += 1

        if number_of_moves == 9 and not check_victory() and not  check_defeat():
            print(f"___________.__        \n"
                  f"\__    ___/|__| ____  \n"
                   f" |    |   |  |/ __ \ \n"
                    f"|    |   |  \  ___/ \n"
                    f"|____|   |__|\___  >\n"
                    f"               \/ \n")
            print("Try again.")

            game_on = False


game()
