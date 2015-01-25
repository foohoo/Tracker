__author__ = 'Baron'

import pygame, sys, Tracker, glob
from pygame.locals import *
from Tracker import *

pygame.init()
pygame.display.set_caption('Tracker')


def display_message(text):
    textSurfaceObj = fontObj.render(text, True, TRONBLUELIGHT, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def draw_level(levelNo):
    level = Level(levels[levelNo])
    for wall in level.walls:
        pygame.draw.rect(DISPLAYSURF, TRONBLUEDARK, wall)

    return level


def get_levels():
    levels = []
    map_files = glob.iglob("./*.txt")

    for map_file in map_files:
        with open(map_file) as level_txt:
            map_data = []
            for line in level_txt:
                map_data.append(line.strip())

        levels.append(map_data)

    return levels

#Set Constants
WIN_WIDTH = 912
WIN_HEIGHT = 608

DARKBLUE = (0, 25, 82)
RED = (255, 0, 0)
DARKRED = (97, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (5, 13, 16)
TRONBLUEDARK = (52, 96, 141)
TRONBLUELIGHT = (24, 202, 230)
#End Constants

#Setup game surface
DISPLAYSURF = pygame.display.set_mode((900, 600))
DISPLAYSURF.fill(BLACK)
FPS = 150
fpsClock = pygame.time.Clock()
#End setup game surface

#global variables
fontObj = pygame.font.Font('freesansbold.ttf', 95)
levelNo = 0
levels = get_levels()
#end global variables

level = draw_level(levelNo)

tracker = Tracker(WIN_HEIGHT, WIN_WIDTH, level.starty-8)
pygame.draw.rect(DISPLAYSURF, TRONBLUELIGHT, tracker.player)

while True:
    while not tracker.dead and not tracker.win:

        tracker.move_player()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                tracker.check_direction(event.key)

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(DISPLAYSURF, TRONBLUELIGHT, tracker.player)
        tracker.check_collision(level.walls, level.end_rect1, level.end_rect2)

        pygame.display.update()
        fpsClock.tick(FPS)

    #game has ended
    if tracker.dead:
        display_message('Game Over!')
    else:
        display_message('Complete!')
        levelNo += 1

    while tracker.dead or tracker.win:
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == K_RETURN:
                        DISPLAYSURF.fill(BLACK)
                        level = draw_level(levelNo)
                        tracker = Tracker(WIN_HEIGHT, WIN_WIDTH, level.starty-8)

        pygame.display.update()
        fpsClock.tick(FPS)