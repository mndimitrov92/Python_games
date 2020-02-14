import sys

import pygame
from pygame.locals import *

from gameobjects.vector2D import Vector2D

SPRITE_IMG = "bird.png"

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

clock = pygame.time.Clock()

position = Vector2D(100.0, 100.0)
speed = 250
heading = Vector2D()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            destination = Vector2D(*event.pos) - (Vector2D(*sprite.get_size()) / 2)
            heading = Vector2D.from_points(position, destination)
            heading.normalize()
    screen.blit(sprite, (position.x, position.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    position += heading * distance_moved
    pygame.display.update()
