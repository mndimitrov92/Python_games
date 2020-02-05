import random
import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))

for _ in range(30):
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    random_pos = (random.randint(0, 639), random.randint(0, 480))
    random_radius = random.randint(1, 100)
    pygame.draw.circle(screen, random_color, random_pos, random_radius)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
