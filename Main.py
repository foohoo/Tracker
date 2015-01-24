__author__ = 'Baron'

import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Tracker')

#Set Constants
WIN_WIDTH = 900
WIN_HEIGHT = 600
DARKBLUE = (0, 25, 82)
RED = (255, 0, 0)
#End Constants

#Setup game surface
DISPLAYSURF = pygame.display.set_mode((900, 600))
DISPLAYSURF.fill(DARKBLUE)
FPS = 150
fpsClock = pygame.time.Clock()
#End setup game surface

#global variables
direction = 'right'
playerx = 10
playery = WIN_HEIGHT/2
#end global variables

player = pygame.draw.rect(DISPLAYSURF, RED, (playerx, playery, 10, 10))


def move_player(x, y, move_direction):
    if move_direction == 'right':
        x += 1
    elif move_direction == 'up':
        y += -1
    elif move_direction == 'down':
        y += 1
    else:
        x += 1
    return x, y


def check_direction(key, current_direction):
    if key == K_DOWN:
        if current_direction != 'up':
            return 'down'

    if key == K_RIGHT:
        return 'right'

    if key == K_UP:
        if current_direction != 'down':
            return 'up'

    return current_direction

while True:

    playerx, playery = move_player(playerx, playery, direction)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            direction = check_direction(event.key, direction)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player = pygame.draw.rect(DISPLAYSURF, RED, (playerx, playery, 10, 10))
    pygame.display.update()
    fpsClock.tick(FPS)
