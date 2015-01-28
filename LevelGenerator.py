__author__ = 'Baron'

import sys
from random import randint

WIDTH = 51
HEIGHT = 32


def reset_generator():
    global y, x, level, start_point, down_coord, up_coord, right_coord, direction, current_direction, previous_directions
    level = [['W' for x in range(WIDTH)] for y in range(HEIGHT)]
    start_point = 0
    down_coord = up_coord = right_coord = (0, 0)
    direction = ('right', 'up', 'down')
    current_direction = 'right'
    previous_directions = ['', '']


def write_to_file():
    file = open("level.txt", 'w')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            file.write(level[y][x])
        file.write("\n")


def generate_start_point():
    global start_point
    global down_coord, up_coord, right_coord

    start_point = randint(4, 28)
    level[start_point - 1][0] = 'O'
    level[start_point][0] = 'S'
    level[start_point + 1][0] = 'S'
    level[start_point + 2][0] = 'O'

    for x in range(1,8):
        level[start_point][x] = 'T'
        level[start_point + 1][x] = 'T'

    down_coord = ([6], [start_point+2])
    up_coord = ([6], [start_point-1])
    right_coord = ([8], [start_point])


def move_right():
    global down_coord, up_coord, right_coord

    level[right_coord[1][0]][right_coord[0][0]] = 'R'
    level[(right_coord[1][0]) + 1][right_coord[0][0]] = 'R'

    right_coord[0][0] += 1
    up_coord[0][0] += 1
    down_coord[0][0] += 1


def move_up():
    global down_coord, up_coord, right_coord

    if right_coord[1][0] <= 3:
        return

    level[up_coord[1][0]][up_coord[0][0]] = 'U'
    level[up_coord[1][0]][(up_coord[0][0] + 1)] = 'U'
    right_coord[1][0] -= 1
    up_coord[1][0] -= 1
    down_coord[1][0] -= 1


def move_down():
    global down_coord, up_coord, right_coord

    if right_coord[1][0] >= 27:
        return

    level[down_coord[1][0]][down_coord[0][0]] = 'D'
    level[down_coord[1][0]][(down_coord[0][0] + 1)] = 'D'
    right_coord[1][0] += 1
    up_coord[1][0] += 1
    down_coord[1][0] += 1


def end_level():
    global down_coord, up_coord, right_coord

    for x in range(6):
        move_right()

    level[(right_coord[1][0] - 1)][right_coord[0][0]] = 'O'
    level[(right_coord[1][0])][right_coord[0][0]] = 'E'
    level[(right_coord[1][0]) + 1][right_coord[0][0]] = 'E'
    level[(right_coord[1][0]) + 2][right_coord[0][0]] = 'O'


def generate_level():
    global current_direction, previous_directions

    reset_generator()
    generate_start_point()

    while right_coord[0][0] < 44:
        change = randint(1,100)

        if ((current_direction == 'right' and change >= 20) or (current_direction != 'right' and change >= 90)):
            new_direction = direction[randint(0, 2)]
            while current_direction == new_direction:
                new_direction = direction[randint(0, 2)]
            current_direction = new_direction

        if current_direction == 'right':
            move_right()
            move_right()
            previous_directions[0] = previous_directions[1]
            previous_directions[1] = current_direction
        elif current_direction == 'down'and previous_directions[1] != 'up' and not (previous_directions[1] == 'right' and previous_directions[0] == 'up'):
            move_down()
            move_down()
            previous_directions[0] = previous_directions[1]
            previous_directions[1] = current_direction
        elif current_direction == 'up' and previous_directions[1] != 'down' and not (previous_directions[1] == 'right' and previous_directions[0] == 'down'):
            move_up()
            move_up()
            previous_directions[0] = previous_directions[1]
            previous_directions[1] = current_direction

    end_level()
    # write_to_file()

    level_array = []
    for x in range(HEIGHT):
        line = ''
        for y in range(WIDTH):
            line = line + level[x][y]
        level_array.append(line)

    return level_array



