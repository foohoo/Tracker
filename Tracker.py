__author__ = 'Baron'

import pygame, sys
from pygame.locals import *


class Player():

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 16, 16)


class Tracker():

    def __init__(self, win_height, win_width, starty):
        self.direction = 'right'
        self.player = Player(10, starty)
        self.win_height = win_height
        self.win_width = win_width
        self.gameEnded = False

    def move_player(self):
        if self.direction == 'right':
            self.player.rect.x += 1
        elif self.direction == 'up':
            self.player.rect.y += -1
        elif self.direction == 'down':
            self.player.rect.y += 1
        else:
            self.player.rect.x += 1

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

    def check_collision(self, walls, endrect1, endrect2):
        if self.player.rect.y < 0 or self.player.rect.y > self.win_height:
            self.gameEnded = True

        if self.player.rect.x < 0 or self.player.rect.x > self.win_width:
            self.gameEnded = True

        for wall in walls:
            if self.player.rect.colliderect(wall.rect):
                self.gameEnded = True

        if self.player.rect.colliderect(endrect1) or self.player.rect.colliderect(endrect2):
            self.gameEnded = True

        return