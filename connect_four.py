import sys

import numpy as np
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROWS = 6
COLUMNS = 7
PLAYER1 = 1
PLAYER2 = 2
CUBE_SIZE = 80
SCREEN_SIZE = (CUBE_SIZE * COLUMNS, CUBE_SIZE * COLUMNS)
CIRCLE_RADIUS = (CUBE_SIZE // 2) - 5  # Needs to be a bit smaller than the cube

# Initialize the game
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Connect for game")
screen.fill(BLACK)
width, height = SCREEN_SIZE
my_font = pygame.font.SysFont("monospace", 75)


def create_board():
    """ Create the initial state of the board with 0s"""
    board = np.zeros((ROWS, COLUMNS))
    return board


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def get_next_open_row(board, column):
    for row in range(ROWS):
        if board[row][column] == 0:
            return row


def is_valid_location(board, column):
    return board[ROWS - 1][column] == 0


def print_board(board):
    print(np.flip(board, 0))


def is_winning_move(board, piece):
    # Check horizontal locations for win
    for col in range(COLUMNS - 3):
        for row in range(ROWS):
            if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and \
                    board[row][col + 3] == piece:
                return True

    # Check vertical locations for win
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and \
                    board[row + 3][col] == piece:
                return True

    # Check positively sloped diagonals
    for col in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and \
                    board[row + 3][col + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for col in range(COLUMNS - 3):
        for row in range(3, ROWS):
            if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and \
                    board[row - 3][col + 3] == piece:
                return True


def draw_board(board):
    for col in range(COLUMNS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE, (col * CUBE_SIZE, row * CUBE_SIZE + CUBE_SIZE, CUBE_SIZE, CUBE_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(col * CUBE_SIZE + CUBE_SIZE / 2), int(row * CUBE_SIZE + CUBE_SIZE + CUBE_SIZE / 2)), CIRCLE_RADIUS)

    for col in range(COLUMNS):
        for row in range(ROWS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (
                    int(col * CUBE_SIZE + CUBE_SIZE / 2), height - int(row * CUBE_SIZE + CUBE_SIZE / 2)), CIRCLE_RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(col * CUBE_SIZE + CUBE_SIZE / 2), height - int(row * CUBE_SIZE + CUBE_SIZE / 2)), CIRCLE_RADIUS)


board = create_board()
draw_board(board)
game_over = False
turn = PLAYER1

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            # For the circle visualization over the board
            pygame.draw.rect(screen, BLACK, (0, 0, width, CUBE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(CUBE_SIZE / 2)), CIRCLE_RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(CUBE_SIZE / 2)), CIRCLE_RADIUS)
        pygame.display.update()
        if event.type == MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, CUBE_SIZE))
            # Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(posx // CUBE_SIZE)
                # Check location
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER1)
                    # Check if is winning
                    if is_winning_move(board, PLAYER1):
                        label = my_font.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
            # Player 2 Input
            else:
                posx = event.pos[0]
                col = int(posx // CUBE_SIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER2)

                    if is_winning_move(board, PLAYER2):
                        label = my_font.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
            turn += 1
            turn = (turn % 2)
            draw_board(board)

            if game_over:
                pygame.time.wait(3000)
