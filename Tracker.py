__author__ = 'Baron'

import pygame, sys
from pygame.locals import *


class Level():

    def __init__(self, level):
        self.walls = []
        self.starty = 0
        self.end_rect1 = pygame.Rect(0, 0, 16, 16)
        self.end_rect2 = pygame.Rect(0, 0, 16, 16)

        self.load_level(level)

    def load_level(self, level):
        x = y = 48
        for row in level:
            for col in row:
                if col == "W":
                    self.walls.append(pygame.Rect(x, y, 16, 16))
                if col == "E":
                    self.end_rect1 = pygame.Rect(x, y, 16, 16)
                    self.end_rect2 = pygame.Rect(x, y, 16, 16)
                if col == "S":
                    self.starty = y
                x += 16
            y += 16
            x = 48


class Player():

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 16, 16)


class Tracker():

    def __init__(self, win_height, win_width, starty):
        self.direction = 'right'
        self.player = Player(10, starty)
        self.win_height = win_height
        self.win_width = win_width
        self.dead = False
        self.win = False

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
            self.dead = True

        if self.player.rect.x < 0 or self.player.rect.x > self.win_width:
            self.dead = True

        for wall in walls:
            if self.player.rect.colliderect(wall):
                self.dead = True

        if self.player.rect.colliderect(endrect1) or self.player.rect.colliderect(endrect2):
            self.win = True

        return