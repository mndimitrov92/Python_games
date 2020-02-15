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

sprite_pos = Vector2D(200, 150)
sprite_speed = 800

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed_key = pygame.key.get_pressed()
    key_direction = Vector2D(0, 0)

    if pressed_key[K_LEFT]:
        key_direction.x = -1
    elif pressed_key[K_RIGHT]:
        key_direction.x = 1

    if pressed_key[K_UP]:
        key_direction.y = -1
    elif pressed_key[K_DOWN]:
        key_direction.y = 1

    key_direction.normalize()

    screen.blit(sprite, (sprite_pos.x, sprite_pos.y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_pos += key_direction * sprite_speed * time_passed_seconds
    pygame.display.update()
