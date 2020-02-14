import sys

import pygame
from pygame.locals import *

CHARACTER = "character.png"

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))
character = pygame.image.load(CHARACTER).convert_alpha()

# The clock object
clock = pygame.time.Clock()
# x coordinate of the character
x = 0
# Speed in pixels per second
speed = 250

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(character, (x, 220))
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    distance_moved = time_passed_seconds * speed
    x += distance_moved
    if x > 640:
        x -= 640
    pygame.display.update()
