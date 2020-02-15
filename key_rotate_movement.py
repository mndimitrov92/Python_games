import math
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
sprite_speed = 300
sprite_rotation = 0
sprite_rotation_speed = 360  # Degrees per second

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    rotation_direction = 0
    movement_direction = 0

    if pressed_keys[K_UP]:
        movement_direction = +1
    if pressed_keys[K_DOWN]:
        movement_direction = -1
    if pressed_keys[K_LEFT]:
        rotation_direction = -1
    if pressed_keys[K_RIGHT]:
        rotation_direction = +1

    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2D(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, (sprite_draw_pos.x, sprite_draw_pos.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    heading_x = math.sin(sprite_rotation * math.pi / 180.0)
    heading_y = math.cos(sprite_rotation * math.pi / 180.0)
    heading = Vector2D(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds
    pygame.display.update()
