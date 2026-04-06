"""
Name:Luke Balducci
Description: Human versus human tictactoe game. 3x3 board with x and o 
Date: 4//6/2026
log:
bugs: users cant play again after finishing playing the game.

"""
import random

def display_board(board):
    print()
    print("      Col 1 Col 2 Col 3")
    print("Row 1  " + board[0][0] + "  |  " + board[0][1] + "  |  " + board[0][2])
    print("      -----------------")
    print("Row 2  " + board[1][0] + "  |  " + board[1][1] + "  |  " + board[1][2])
    print("      -----------------")
    print("Row 3  " + board[2][0] + "  |  " + board[2][1] + "  |  " + board[2][2])
    print()

def get_player_move(board, player):
    while True:
        print("Player " + player + ", it's your turn!")
        row_input = input("Enter row (1, 2, or 3): ")
        col_input = input("Enter column (1, 2, or 3): ")

        if row_input.isdigit() == False or col_input.isdigit() == False:
            print("Invalid input. Please enter numbers only.")
            continue

        row = int(row_input)
        col = int(col_input)

        if row < 1 or row > 3:
            print("Invalid row. Please enter a number between 1 and 3.")
            continue

        if col < 1 or col > 3:
            print("Invalid column. Please enter a number between 1 and 3.")
            continue

        if board[row - 1][col - 1] != " ":
            print("That cell is already taken. Choose a different one.")
            continue

        return row - 1, col - 1

def check_winner(board, player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_game():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    print()
    print("   XOXO -TIC TAC TOE- XOXO")
    print()

    name1 = input("Enter Player 1's name: ")
    name2 = input("Enter Player 2's name: ")

    # List of both player names to pick from
    names = [name1, name2]

    print()
    print("Welcome " + name1 + " and " + name2 + "!")
    print()

    choice = input("Would you like to choose who is X and O, or pick randomly? Enter 1 for random or 2 for custom: ")

    if choice == "1":
        # Shuffle the list and assign X and O randomly
        random.shuffle(names)
        x_player = names[0]
        o_player = names[1]
        print()
        print("Randomly selected: " + x_player + " is X and goes first!")
        print(o_player + " is O.")

    elif choice == "2":
        print()
        pick = input("Who wants to be X? X goes first. Enter 1 for " + name1 + " or 2 for " + name2 + ": ")

        if pick == "1":
            x_player = names[0]
            o_player = names[1]
            print(name1 + " is X and goes first!")
        elif pick == "2":
            x_player = names[1]
            o_player = names[0]
            print(name2 + " is X and goes first!")
        else:
            print("Invalid choice, randomly assigning roles instead.")
            random.shuffle(names)
            x_player = names[0]
            o_player = names[1]
            print(x_player + " is X and goes first!")

    else:
        print("Invalid choice, randomly assigning roles instead.")
        random.shuffle(names)
        x_player = names[0]
        o_player = names[1]
        print(x_player + " is X and goes first!")

    print()
    current_player = "X"

    while True:
        display_board(board)

        if current_player == "X":
            current_name = x_player
        else:
            current_name = o_player

        row, col = get_player_move(board, current_name)

        board[row][col] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print("Player " + current_player + " (" + current_name + ") wins! Good Game!")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw! Good game " + name1 + " and " + name2 + "!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()