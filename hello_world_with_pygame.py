#!/usr/bin/env python3
# This is my first script with pygame

import pygame
import sys
from pygame.locals import *

BACKGROUND_IMAGE_FILE = 'bird.png'
MOUSE_IMAGE_FILE = 'image4.jpeg'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello World")

background = pygame.image.load(BACKGROUND_IMAGE_FILE).convert()
mouse_cursor = pygame.image.load(MOUSE_IMAGE_FILE).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        screen.blit(background, (0, 0))

        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))

        pygame.display.update()