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
        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)

    screen.fill((255, 255, 255))

    if len(points) >= 3:
        pygame.draw.polygon(screen, (250, 0, 60), points)
    for point in points:
        pygame.draw.circle(screen, (50, 0, 250), point, 3)

    pygame.display.update()
