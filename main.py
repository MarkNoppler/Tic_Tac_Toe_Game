"""
What it is:
A two player text-based Tic Tac Toe game

How to use it:
Run the code then follow the instructions in the interpreter. Enter a value between 0 2 (with a space) to insert either
an X or a O on the corresponding players turn. First number refers to the columns, the second refers to the rows.

Made by Jacob Fairhurst
"""

def print_board(board):
    """Function to initialise the play area. Loops through each to draw an ascii grid"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Checks the board each turn for a winner by iterating through rows.
    Uses range of 3 to indentify players markers in either a single row, column or diagonal.
    Will return True if a player wins. Will return False if none of these conditions are met."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all (board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Checks if the board is full. If spaces are still available and returns the board."""
    return all(cell !=" " for row in board for cell in row)


def tic_tac_toe():
    """Function to the run the game.
    Initialises the board 3x3 for play and a list of two players for X and O.
    Allows players to type an input of a grid coordinate to enter their marker on a turn.
    Runs a while loop to check the status of the game and initialises a turn counter.
    Map function parses player input from string to integer.
    Check_winner() function determines if the current player has won.
    Is_full function() called on each turn to check the status of the game, a draw will be declared if no spaces exist.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row, col = -1, -1
        while row not in range(3) or col not in range(3) or board[row][col] != " ":
            try:
                row, col = map(int, input(f"Player {players[turn]}, enter a row and column (0-2)").split())
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
                continue

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It is a draw!")
            break

        turn = 1 - turn




#call the function to play
tic_tac_toe()