__author__ = 'Baron'

import pygame, sys, Tracker, glob, time, LevelGenerator, Intro
from pygame.locals import *
from Tracker import *
from LevelGenerator import *
from Intro import *

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.display.set_caption('Tracker')
DISPLAYSURF = pygame.display.set_mode((900, 600))


def display_message(text, x, y, font):
    textSurfaceObj = font.render(text, True, TRONBLUELIGHT, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def draw_generated_level(gen_level):
    for wall in gen_level.walls:
        pygame.draw.rect(DISPLAYSURF, TRONBLUEDARK, wall)


def draw_scoreboard(score, lives):
    display_message("SCORE: "+ str(score) + "    LIVES: " + str(lives), 260, 20, smallFont)


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


def start_level(last_level):
    global tracker
    DISPLAYSURF.fill(BLACK)

    if last_level is None:
        new_level = Level(generate_level())
    else:
        new_level = last_level

    draw_generated_level(new_level)
    draw_scoreboard(score, lives)
    new_tracker = Tracker(WIN_HEIGHT, WIN_WIDTH, new_level.starty-8)

    pygame.display.update()
    time.sleep(1.5)

    return new_level, new_tracker


def direction_key(key):
    return key == K_UP or key == K_DOWN or key == K_RIGHT


def flash_player():
    count = 0
    while count < 10:
        if count % 2 == 0:
            pygame.draw.rect(DISPLAYSURF, BLACK, tracker.player)
        else:
            pygame.draw.rect(DISPLAYSURF, TRONBLUELIGHT, tracker.player)
        pygame.display.update()
        time.sleep(0.1)

        count += 1


#Set Constants
WIN_WIDTH = 912
WIN_HEIGHT = 608
BLACK = (5, 13, 16)
TRONBLUEDARK = (52, 96, 141)
TRONBLUELIGHT = (24, 202, 230)
WHITE = (255, 255, 255)
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
largeFont = pygame.font.Font('TRON.ttf', 80)
smallFont = pygame.font.Font('IRRESIST.ttf', 40)
score = 0
lives = 3
#end global variables

Intro.start(DISPLAYSURF)

level, tracker = start_level(None)

while True:

    while not tracker.dead and not tracker.win:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if direction_key(event.key):
                    turn.play()
                    tracker.check_direction(event.key)
                    break

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        tracker.check_collision(level.walls)

        if tracker.dead:
            boom.play()
            flash_player()
            pygame.event.clear()
            lives -= 1
            if lives < 0:
                display_message("""Game Over!""", WIN_WIDTH/2, WIN_HEIGHT/2, largeFont)
        elif tracker.win:
            complete.play()
            display_message('Complete!', WIN_WIDTH/2, WIN_HEIGHT/2, largeFont)
            score += 1
        else:
            tracker.move_player()
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
                else:
                    if tracker.dead and lives < 3:
                        if lives < 0:
                            lives = 3
                            score = 0
                            Intro.start(DISPLAYSURF)
                        level, tracker = start_level(level)
                    else:
                        level, tracker = start_level(None)
                    break
