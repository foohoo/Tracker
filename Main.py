__author__ = 'Baron'

import pygame, sys, Tracker
from pygame.locals import *
from Tracker import *

pygame.init()
pygame.display.set_caption('Tracker')

#Set Constants
WIN_WIDTH = 912
WIN_HEIGHT = 608

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

fontObj = pygame.font.Font('freesansbold.ttf', 95)
textSurfaceObj = fontObj.render('Game Over!', True, RED, DARKBLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2 )

walls = []
level = []

with open('level1.txt') as leveltxt:
    for line in leveltxt:
        level.append(line.strip())

#end global variables


class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

x = y = 48
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect1 = pygame.Rect(x, y, 16, 16)
            end_rect2 = pygame.Rect(x, y, 16, 16)
        if col == "S":
            starty = y
        x += 16
    y += 16
    x = 48

for wall in walls:
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), wall.rect)

tracker = Tracker(WIN_HEIGHT, WIN_WIDTH, starty-4)
player = pygame.draw.rect(DISPLAYSURF, RED, tracker.player)

while True:
    while not tracker.gameEnded:

        tracker.move_player()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                tracker.check_direction(event.key)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player = pygame.draw.rect(DISPLAYSURF, RED, tracker.player)

        tracker.check_collision(walls, end_rect1, end_rect2)

        pygame.display.update()
        fpsClock.tick(FPS)

    #game has ended

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    DISPLAYSURF.fill(DARKBLUE)
                    tracker = Tracker(WIN_HEIGHT, WIN_WIDTH)

    pygame.display.update()
    fpsClock.tick(FPS)