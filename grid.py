import pygame
import numpy as np
import random


class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size)
        self.offset = offset

    def random_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)

    def conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos = x * self.scale
                y_pos = y * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color,
                                     [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])

                else:
                    pygame.draw.rect(surface, off_color,
                                     [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])

        update = np.ndarray(shape=self.size)
        if not pause:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours(x, y)

                    if state == 0 and neighbours == 3:
                        update[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        update[x][y] = 0
                    else:
                        update[x][y] = state

            self.grid_array = update

    def clear_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 0

    def handle_left_mouse(self, x, y):
        _x = x // self.scale
        _y = y // self.scale

        if self.grid_array[_x][_y] is not None:
            self.grid_array[_x][_y] = 1

    def handle_right_mouse(self, x, y):
        _x = x // self.scale
        _y = y // self.scale

        if self.grid_array[_x][_y] is not None:
            self.grid_array[_x][_y] = 0

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n + self.rows) % self.rows
                y_edge = (y + m + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
