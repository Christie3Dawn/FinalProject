# Connect Four Game

import numpy as np
import pygame
import sys
import math

# Define global (static) variables
BLUE = (30, 144, 255)
BLACK = (0, 0, 0)
EMPTY = (40, 79, 105)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
ROWCNT = 6
COLCNT = 7

def create_board():
    board = np.zeros((6,7))
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
            if board[r][c] == token and board[r+1][c+1] == token and board[r+2][c+2] == token and board[r+3][c+3] == \
                    token:
                return True

    # Checks for diagonal down win
    for c in range(COLCNT-3):
        for r in range(3, ROWCNT):
            if board[r][c] == token and board[r-1][c+1] == token and board[r-2][c+2] == token and board[r-3][c+3] == \
                    token:
                return True

def draw_board(board):
    # for loop to build background
    for c in range(COLCNT):
        for r in range(ROWCNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE, r * SQUARE + SQUARE, SQUARE, SQUARE))
            pygame.draw.circle(screen, EMPTY, (int(c * SQUARE + SQUARE/2),
                                               int(r * SQUARE + SQUARE + SQUARE/2)), RADIUS)

    # for loop to fill in tokens
    for c in range(COLCNT):
        for r in range(ROWCNT):
            if board[r][c] == 1:  # Player 1 moves red
                pygame.draw.circle(screen, RED, (int(c * SQUARE + SQUARE / 2),
                                                 height - int(r * SQUARE + SQUARE / 2)), RADIUS)
            elif board[r][c] == 2:  # Player 2 moves yellow
                pygame.draw.circle(screen, GOLD, (int(c * SQUARE + SQUARE / 2),
                                                  height - int(r * SQUARE + SQUARE / 2)), RADIUS)

    pygame.display.update()  # Shows screen with new updates (moves)

board = create_board()
print_board(board)
game_over = False
turn = 0

# Initializing pygame
pygame.init()

SQUARE = 100    # in pixels
width = COLCNT * SQUARE
height = (ROWCNT + 1) * SQUARE
size = (width, height)
RADIUS = int(SQUARE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 45)

# Main game loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Tracks mouse with token before move
        if event.type == pygame.MOUSEMOTION:
            # Draws black rectangle so mouse tracking does not create a red/yellow blob
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, GOLD, (posx, int(SQUARE / 2)), RADIUS)
        pygame.display.update()    # Shows screen with new updates (moves)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE))
            #print(event.pos) # Prints (shows the coordinates where the screen was clicked)
            # Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                # takes the x position/ 100 (or SQUARE) to get a number 1-6 like Step1.
                # Floor to round down to nearest integer
                selection = int(math.floor(posx/SQUARE))

                if valid_location(board, selection):
                    row = next_open_row(board, selection)
                    drop_token(board, row, selection, 1)     # Puts '1' on board in spot player 1 drops their token

                    if win(board, 1):
                        label = myfont.render("Player 1 WINS! Game Over", 1, RED)
                        screen.blit(label, (20, 10))
                        game_over = True

            # Player 2 Input
            else:
                posx = event.pos[0]
                selection = int(math.floor(posx/SQUARE))

                if valid_location(board, selection):
                    row = next_open_row(board, selection)
                    drop_token(board, row, selection, 2)

                    if win(board, 2):
                        label = myfont.render("Player 2 WINS! Game Over", 1, GOLD)
                        screen.blit(label, (20, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(4000)


# Resources
#https://www.dataquest.io/blog/python-projects-for-beginners/
#https://www.edureka.co/blog/python-projects/
#https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ
#https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html
#https://storm-coder-dojo.github.io/activities/python/connect-four.html
#https://www.pygame.org/docs/
#https://inventwithpython.com/pygame/chapter2.html
#http://inventwithpython.com/pygame/chapter10.html
#https://www.youtube.com/watch?v=XGf2GcyHPhc
#https://www.rapidtables.com/web/color/index.html
#https://pythonguides.com/python-pygame-tutorial/