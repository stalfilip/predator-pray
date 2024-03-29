import sys
import pygame
import random
from threading import Thread
import engine

random.seed(None)
size = width, height = 1000, 1000
play_width = width/5
play_height = height/5
is_stopped = False

# These are the codes that pygame uses, I am not sure what format it is
dark_green = (0 << 16) | (50 << 8) | 0
red = (139 << 16) | (0 << 8) | 0
blue = (0 << 16) | (0 << 8) | 100
color_arr = [dark_green, red, blue]
pygame.init()
screen = pygame.display.set_mode(size)
pp = engine.Map()


# Paints a 3x3 square for each node
def paint(x, y, color_int):
    screen.set_at((x, y), color_arr[color_int])
    screen.set_at((x + 1, y), color_arr[color_int])
    screen.set_at((x, y + 1), color_arr[color_int])
    screen.set_at((x + 1, y + 1), color_arr[color_int])
    screen.set_at((x + 2, y), color_arr[color_int])
    screen.set_at((x, y + 2), color_arr[color_int])
    screen.set_at((x + 2, y + 2), color_arr[color_int])
    screen.set_at((x + 2, y + 1), color_arr[color_int])
    screen.set_at((x + 1, y + 2), color_arr[color_int])


# Creates random colors TESTING ONLY
def random_colors(w, h):
    ra = random.randint
    pa = paint
    while not is_stopped:
        for x in range(5, w, 5):
            for y in range(5, h, 5):
                color_int = ra(1, 2)
                pa(x, y, color_int)


# Paints the species at each point on the play board
def paint_map(board):
    pa = paint
    length = len(board)
    for x in range(0, length):
        for y in range(0, length):
            pa(x*5, y*5, board[x][y].species)


pygame.display.set_caption('Predator-prey')
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Game loop, paints the map then calculates the next turn
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_stopped = True
            sys.exit(0)
    paint_map(pp.get_board())
    pygame.display.flip()
    pp.turn()