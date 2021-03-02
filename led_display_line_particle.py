import pygame
from led_display_particle import Particle
from led_display_enum import *

class LineParticle(Particle):
    def __init__(self, pos1, pos2, dir, speed, color):
        Particle.__init__(self)
        self._pos1 = pos1
        self._pos2 = pos2
        self._dir = dir
        self._speed = speed
        self._color = color

    def update(self):
        Particle.update(self)

        if self._dir == Direction.UP:
            self._pos1[1] += self._speed
            self._pos2[1] += self._speed
            if self._pos1[1] < 0:
                self._is_complete = True
        elif self._dir == Direction.DOWN:
            self._pos1[1] += self._speed
            self._pos2[1] += self._speed
            if self._pos1[1] >= self._config.led_row:
                self._is_complete = True
        elif self._dir == Direction.LEFT:
            self._pos1[0] += self._speed
            self._pos2[0] += self._speed
            if self._pos2[0] < 0:
                self._is_complete = True
        elif self._dir == Direction.RIGHT:
            self._pos1[0] += self._speed
            self._pos2[0] += self._speed
            if self._pos1[0] >= self._config.led_col:
                self._is_complete = True


    def paint(self, led_surface):
        Particle.paint(self, led_surface)

        pygame.draw.line(led_surface, self._color, self._pos1, self._pos2)
