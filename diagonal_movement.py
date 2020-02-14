import sys

import pygame
from pygame.locals import *

CHARACTER = "character.png"
pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))
character = pygame.image.load(CHARACTER).convert_alpha()

clock = pygame.time.Clock()

x, y = 100, 100
speed_x, speed_y = 133, 170

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(character, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    # If the character goes beyond the edge of the screen
    # make it move  in the opposite direction
    if x > 640 - character.get_width():
        speed_x = -speed_x
        x = 640 - character.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > 480 - character.get_height():
        speed_y = -speed_y
        y = 480 - character.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()
