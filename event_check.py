# Script for testing pygame events
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (320, 200)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        print(event)

    pygame.display.update()
