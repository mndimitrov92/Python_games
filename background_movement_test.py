import pygame
from pygame.locals import *
import sys

BACKGROUND_IMAGE = 'bird.png'
DISPLAY_SIZE = (540, 480)
pygame.init()

screen = pygame.display.set_mode(DISPLAY_SIZE, 0, 32)
pygame.display.set_caption("Picture movement test")

background = pygame.image.load(BACKGROUND_IMAGE).convert()
x_pos, y_pos = (0, 0)
move_x, move_y = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Movement events
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -10
            elif event.key == K_RIGHT:
                move_x = 10
            elif event.key == K_UP:
                move_y = -10
            elif event.key == K_DOWN:
                move_y = 10

        elif event.type == KEYUP:
            if event.key in [K_LEFT, K_RIGHT]:
                move_x = 0
            elif event.key in [K_UP, K_DOWN]:
                move_y = 0

        x_pos += move_x
        y_pos += move_y
        screen.fill((0, 90, 0))
        screen.blit(background, (x_pos, y_pos))

        pygame.display.update()
