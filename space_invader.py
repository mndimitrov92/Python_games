import math
import random
import sys

import pygame
from pygame import mixer
from pygame.locals import *

SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)

pygame.init()

# Add the screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Title and Icon
icon = pygame.image.load("ufo.png").convert()
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")

# Background image
background = pygame.image.load("background.jpg").convert()
# Background sound
# mixer.music.load("background.wav")
# mixer.music.play(-1)


# Player
player_img = pygame.image.load("spaceship.png").convert_alpha()
player_x = 370
player_y = 480
player_change = 0

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

game_over_txt = pygame.font.Font("freesansbold.ttf", 32)


def game_over_text():
    game_over = game_over_txt.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(game_over, (300, 250))


def show_score(x, y):
    score_var = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_var, (x, y))


# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_xchange = []
enemy_ychange = []
num_of_enemies = 5
for enemy in range(num_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png").convert_alpha())
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_xchange.append(2)
    enemy_ychange.append(40)

# Bullet
bullet_img = pygame.image.load("bullet.png").convert_alpha()
bullet_x = player_x
bullet_y = player_y
bullet_ychange = 10
# When bullet is in ready state, the bullet cannot be seen
# If state is "fire", the bullet is moving
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(x_enemy, y_enemy, x_bullet, y_bullet):
    distance = math.sqrt(math.pow(x_enemy - x_bullet, 2) + (math.pow(y_enemy - y_bullet, 2)))
    return distance < 27


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


while True:
    screen.fill(BLACK)
    # Add the background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Player movement
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player_change = -5
            if event.key == K_RIGHT:
                player_change = 5
            if event.key == K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # Get the current position of the player
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player_change = 0

    # boundary check for the player
    player_x += player_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # boundary check for the enemy
    for i in range(num_of_enemies):

        # Game over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_xchange[i]
        if enemy_x[i] <= 0:
            enemy_xchange[i] = 4
            enemy_y[i] += enemy_ychange[i]
        elif enemy_x[i] >= 736:
            enemy_xchange[i] = -4
            enemy_y[i] += enemy_ychange[i]
        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            # Add explosion sound
            explosion_sound = mixer.Sound("destroyed.wav")
            explosion_sound.play()

            bullet_y = player_y
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)
        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_ychange

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
