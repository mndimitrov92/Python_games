import random
import sys

import pygame
from pygame.locals import *

SCREEN_SIZE = (640, 480)
WHITE = (255, 255, 255)


class Star(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    screen.fill((0, 0, 0))
    stars = []

    # Add a few starts
    for n in range(200):
        x = float(random.randint(0, 639))
        y = float(random.randint(0, 479))
        speed = float(random.randint(10, 300))
        stars.append(Star(x, y, speed))

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                return
        # Add a new star
        y = float(random.randint(0, 479))
        speed = float(random.randint(10, 300))
        star = Star(640.0, y, speed)
        stars.append(star)
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        # Draw the stars
        for star in stars:
            new_x = star.x - time_passed_seconds * star.speed
            pygame.draw.aaline(screen, WHITE, (new_x, star.y), (star.x + 1, star.y))
            star.x = new_x

        def on_screen(star_check):
            return star_check.x > 0

        # Remove the stars that are not visible anymore
        stars = list(filter(on_screen, stars))

        pygame.display.update()


if __name__ == '__main__':
    run()
