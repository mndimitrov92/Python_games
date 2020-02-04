import pygame
from pygame.locals import *
import sys

BG_IMAGE = "bird.png"
SCREEN_SIZE = (640, 480)
MESSAGE = "This is a test message!"

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Test of scrolly text", "Icon title")
# Set the font
font = pygame.sysfont.SysFont("arial", 80, bold=True, italic=True)
text_surface = font.render(MESSAGE, True, (200, 15, 70))

x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height() / 2)
background = pygame.image.load(BG_IMAGE).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    x -= 2
    if x < -text_surface.get_width():
        x = 0

    screen.blit(text_surface, (x, y - 50))
    screen.blit(text_surface, (x + text_surface.get_width(), y - 50))
    pygame.display.update()
