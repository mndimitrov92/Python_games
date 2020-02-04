# Script for testing how to set the pygame window to full screen
import pygame
from pygame.locals import *
import sys

BG_IMAGE = "bird.png"

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(BG_IMAGE).convert()

full_sceen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_f:
                full_sceen = not full_sceen
                if full_sceen:
                    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.blit(background, (0, 0))
    pygame.display.update()
