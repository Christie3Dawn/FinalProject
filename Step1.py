# Connect Four Game

import numpy as np

# Define global (static) variables
ROWCNT = 6
COLCNT = 7

def create_board():
    board = np.zeros((6,7))  # a matrix of all zeros
    return board

def drop_token(board, row, selection, token):
    board[row][selection] = token

def valid_location(board, selection):  # checking that top row of selected column is empty
    return board[5][selection] == 0

def next_open_row(board, selection):
    for r in range(ROWCNT):
        if board[r][selection] == 0:
            return r      # returns first case where the slot is empty

def print_board(board):       # Flip board over so tokens drop to the bottom
    print(np.flip(board, 0))  # Flipped on 0 of x-axes

def win(board, token):
    # Checks for horizontal win
    for c in range(COLCNT-3):
        for r in range(ROWCNT):
            if board[r][c] == token and board[r][c+1] == token and board[r][c+2] == token and board[r][c+3] == token:
                return True

    # Checks for vertical win
    for c in range(COLCNT):
        for r in range(ROWCNT-3):
            if board[r][c] == token and board[r+1][c] == token and board[r+2][c] == token and board[r+3][c] == token:
                return True

    # Checks for diagonal up win
    for c in range(COLCNT-3):
        for r in range(ROWCNT-3):
            if board[r][c] == token and board[r+1][c+1] == token and board[r+2][c+2] == \
                    token and board[r+3][c+3] == token:
                return True

    # Checks for diagonal down win
    for c in range(COLCNT-3):
        for r in range(3, ROWCNT):
            if board[r][c] == token and board[r-1][c+1] == token and board[r-2][c+2] == \
                    token and board[r-3][c+3] == token:
                return True

board = create_board()
print_board(board)
game_over = False
# Set turn count to 0
turn = 0

while not game_over:
    # Player 1 Input
    if turn == 0:
        selection = int(input("Player 1: Choose the column to drop your token (0-6):"))   # User enters column number

        if valid_location(board, selection):
            row = next_open_row(board, selection)
            drop_token(board, row, selection, 1)     # Puts a 1 on the board in the spot player 1 drops their token

            if win(board, 1):
                print("Player 1 WINS!!! Game Over")
                game_over = True

    # Player 2 Input
    else:
        selection = int(input("Player 2: Choose the column to drop your token (0-6):"))

        if valid_location(board, selection):
            row = next_open_row(board, selection)
            drop_token(board, row, selection, 2)

            if win(board, 2):
                print("Player 2 WINS!!!  Game Over")
                game_over = True

    print_board(board)

    # Increase turn count by 1
    turn += 1
    # Turns by odd and even count
    turn = turn % 2