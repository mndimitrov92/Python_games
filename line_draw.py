import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()

    # note that anti aliased line is slower than drawing a regular line
    for x in range(0, 640, 20):
        pygame.draw.aaline(screen, (255, 0, 0), (x, 0), mouse_pos)
        pygame.draw.aaline(screen, (255, 0, 0), (x, 479), mouse_pos)

    for y in range(0, 480, 20):
        pygame.draw.aaline(screen, (255, 0, 0), (0, y), mouse_pos)
        pygame.draw.aaline(screen, (255, 0, 0), (639, y), mouse_pos)

    pygame.display.update()
