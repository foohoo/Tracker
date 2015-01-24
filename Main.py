__author__ = 'Baron'

import pygame, sys
from pygame.locals import *

WIN_WIDTH = 900
WIN_HEIGHT = 600

pygame.init()

FPS = 150
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((900, 600))
DARKBLUE = (0, 25, 82)
RED = (255, 0, 0)

direction = 'right'

playerx = 10
playery = WIN_HEIGHT/2

player = pygame.draw.rect(DISPLAYSURF, RED, (playerx, playery, 10, 10))


DISPLAYSURF.fill(DARKBLUE)

pygame.display.set_caption('Tracker')
while True:

    if direction == 'right':
        playerx += 1
    elif direction == 'up':
        playery += -1
    elif direction == 'down':
        playery += 1
    else:
        playerx += 1

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if direction != 'up':
                    direction = 'down'
            elif event.key == K_RIGHT:
                direction = 'right'
            elif event.key == K_UP:
                if direction != 'down':
                    direction = 'up'

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player = pygame.draw.rect(DISPLAYSURF, RED, (playerx, playery, 10, 10))
    pygame.display.update()
    fpsClock.tick(FPS)
