import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

points = []
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            points.append(event.pos)
            if len(points) > 100:
                del points[0]
    screen.fill((255, 255, 255))

    if len(points) > 1:
        pygame.draw.aalines(screen, (255, 100, 10), False, points)

    pygame.display.update()
