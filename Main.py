__author__ = 'Baron'

import pygame, sys, Tracker
from pygame.locals import *
from Tracker import *

pygame.init()
pygame.display.set_caption('Tracker')

#Set Constants
WIN_WIDTH = 900
WIN_HEIGHT = 600

DARKBLUE = (0, 25, 82)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
#End Constants

#Setup game surface
DISPLAYSURF = pygame.display.set_mode((900, 600))
DISPLAYSURF.fill(DARKBLUE)
FPS = 150
fpsClock = pygame.time.Clock()
#End setup game surface

#global variables
tracker = Tracker(WIN_HEIGHT, WIN_WIDTH)

fontObj = pygame.font.Font('freesansbold.ttf', 95)
textSurfaceObj = fontObj.render('Game Over!', True, RED, DARKBLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2 )

#end global variables

player = pygame.draw.rect(DISPLAYSURF, RED, (tracker.playerx, tracker.playery, 10, 10))


while True:
    while not tracker.gameEnded:

        tracker.move_player()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                tracker.check_direction(event.key)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player = pygame.draw.rect(DISPLAYSURF, RED, (tracker.playerx, tracker.playery, 10, 10))

        tracker.check_collision()

        pygame.display.update()
        fpsClock.tick(FPS)

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    DISPLAYSURF.fill(DARKBLUE)
                    tracker = Tracker(WIN_HEIGHT, WIN_WIDTH)

    pygame.display.update()
    fpsClock.tick(FPS)