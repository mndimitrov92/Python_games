import sys

import pygame
from pygame.locals import *

CHARACTER_IMG = "character.png"
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))
character = pygame.image.load(CHARACTER_IMG).convert_alpha()

# The x coordinate of the character
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(character, (x, 100))
    x += 1
    # If the character goes of the end of the screen, move it back
    if x > 640:
        x -= 640

    pygame.display.update()
