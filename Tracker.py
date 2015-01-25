__author__ = 'Baron'

import pygame, sys
from pygame.locals import *


class Tracker():

    def __init__(self, win_height, win_width):
        self.direction = 'right'
        self.playerx = 10
        self.playery = win_height/2
        self.win_height = win_height
        self.win_width = win_width
        self.gameEnded = False

    def move_player(self):
        if self.direction == 'right':
            self.playerx += 1
        elif self.direction == 'up':
            self.playery += -1
        elif self.direction == 'down':
            self.playery += 1
        else:
            self.playerx += 1

        return

    def check_direction(self, key):
        if key == K_DOWN:
            if self.direction != 'up':
                self.direction = 'down'

        if key == K_RIGHT:
            self.direction = 'right'

        if key == K_UP:
            if self.direction != 'down':
                self.direction = 'up'

        return

    def check_collision(self):
        if self.playery < 0 or self.playery > self.win_height:
            self.gameEnded = True

        if self.playerx < 0 or self.playerx > self.win_width:
            self.gameEnded = True

        return