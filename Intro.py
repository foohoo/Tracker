__author__ = 'Baron'

import pygame, sys
from pygame.locals import *

TRONBLUELIGHT = (24, 202, 230)
BLACK = (5, 13, 16)
WIN_WIDTH = 912
WIN_HEIGHT = 608
fpsClock = pygame.time.Clock()


def read_intro_text():
    with open("intro.txt") as intro:
        return intro.readlines()[0]


intro_directions = read_intro_text()


def start(surface):
    pen = pygame.Rect(-1, (WIN_HEIGHT/2 + 50), 12, 12)
    surface.fill(BLACK)
    start_game = False
    animation_finished = False
    frame = 0

    while not start_game:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                    start_game = True

        if not animation_finished:
            if intro_directions[frame] == "R":
                pen.x += 1
            if intro_directions[frame] == "U":
                pen.y -= 1
            if intro_directions[frame] == "D":
                pen.y += 1
            if intro_directions[frame] == "L":
                pen.x -= 1

        frame += 1

        if frame >= len(intro_directions):
            animation_finished = True

        pygame.draw.rect(surface, TRONBLUELIGHT, pen)
        pygame.display.update()
        fpsClock.tick(650)