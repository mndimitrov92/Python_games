import pygame
from pygame.locals import *
import sys

BG_IMAGE = 'bird.png'
SCREEN_SIZE = (620, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(BG_IMAGE).convert()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 0)
        pygame.display.set_caption("Screen resized to : %s" %str(event.size))

    screen_w, screen_h = SCREEN_SIZE
    for y in range(0, screen_h, background.get_height()):
        for x in range(0, screen_w, background.get_width()):
            screen.blit(background, (x, y))
    pygame.display.update()

