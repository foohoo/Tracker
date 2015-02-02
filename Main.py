__author__ = 'Baron'

import pygame, sys, Tracker, glob, time, LevelGenerator
from pygame.locals import *
from Tracker import *
from LevelGenerator import *

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.display.set_caption('Tracker')
DISPLAYSURF = pygame.display.set_mode((900, 600))

def display_message(text):
    textSurfaceObj = fontObj.render(text, True, TRONBLUELIGHT, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def draw_generated_level(gen_level):
    for wall in gen_level.walls:
        pygame.draw.rect(DISPLAYSURF, TRONBLUEDARK, wall)


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


def start_level():
    DISPLAYSURF.fill(BLACK)
    new_level = Level(generate_level())
    draw_generated_level(new_level)
    new_tracker = Tracker(WIN_HEIGHT, WIN_WIDTH, new_level.starty-8)
    return new_level, new_tracker

#Set Constants
WIN_WIDTH = 912
WIN_HEIGHT = 608
BLACK = (5, 13, 16)
TRONBLUEDARK = (52, 96, 141)
TRONBLUELIGHT = (24, 202, 230)
#End Constants

#Setup game surface
FPS = 150
fpsClock = pygame.time.Clock()
turn = pygame.mixer.Sound('./Sounds/turn1.wav')
boom = pygame.mixer.Sound('./Sounds/system_shutdown.wav')
complete = pygame.mixer.Sound('./Sounds/complete.wav')
background = pygame.mixer.music.load('./Sounds/background.wav')
pygame.mixer.music.play(-1, 0.0)
#End setup game surface

#global variables
fontObj = pygame.font.Font('TRON.ttf', 80)
#end global variables

level, tracker = start_level()

while True:

    while not tracker.dead and not tracker.win:

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

        tracker.move_player()
        tracker.check_collision(level.walls)

        if tracker.dead:
            boom.play()
            display_message('Game Over!')
        elif tracker.win:
            complete.play()
            display_message('Complete!')
        else:
            pygame.draw.rect(DISPLAYSURF, TRONBLUELIGHT, tracker.player)

        pygame.display.update()
        fpsClock.tick(FPS)

    #game has ended

    while tracker.dead or tracker.win:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_RETURN:
                    level, tracker = start_level()
                    pygame.display.update()
                    time.sleep(1.5)

