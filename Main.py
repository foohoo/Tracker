__author__ = 'Baron'

import pygame, sys, Tracker, glob, time
from pygame.locals import *
from Tracker import *

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
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
    map_files = glob.iglob("./Levels/*.txt")

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
turn = pygame.mixer.Sound('./Sounds/turn1.wav')
boom = pygame.mixer.Sound('./Sounds/system_shutdown.wav')
complete = pygame.mixer.Sound('./Sounds/complete.wav')
background = pygame.mixer.music.load('./Sounds/background.wav')
#End setup game surface

#global variables
fontObj = pygame.font.Font('TRON.ttf', 80)
levelNo = 0
levels = get_levels()
#end global variables

level = draw_level(levelNo)

tracker = Tracker(WIN_HEIGHT, WIN_WIDTH, level.starty-8)
pygame.draw.rect(DISPLAYSURF, TRONBLUELIGHT, tracker.player)
pygame.mixer.music.play(-1, 0.0)

pygame.display.update()
time.sleep(1.5)

while True:

    while not tracker.dead and not tracker.win:

        tracker.move_player()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                turn.play()
                tracker.check_direction(event.key)

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(DISPLAYSURF, TRONBLUELIGHT, tracker.player)
        tracker.check_collision(level.walls)

        pygame.display.update()
        fpsClock.tick(FPS)

    #game has ended
    if tracker.dead:
        boom.play()
        display_message('Game Over!')
    else:
        complete.play()
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
                        time.sleep(1.5)

        pygame.display.update()
        fpsClock.tick(FPS)