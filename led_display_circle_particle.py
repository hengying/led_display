import pygame
from led_display_particle import Particle
from led_display_enum import *

class CircleParticle(Particle):
    def __init__(self, pos, speed, color, line_width):
        Particle.__init__(self)
        self._pos = pos
        self._speed = speed
        self._color = color
        self._line_width = line_width
        self._radius = 1

    def update(self):
        Particle.update(self)

        self._radius += int(self._count * self._speed)

        if self._radius > self._config.led_col + self._config.led_row:
            self._is_complete = True

        r = self._color[0] - 3
        r = 0 if r < 0 else r
        g = self._color[1] - 3
        g = 0 if g < 0 else g
        b = self._color[2] - 3
        b = 0 if b < 0 else b

        self._color = (r, g, b)

    def paint(self, led_surface):
        Particle.paint(self, led_surface)

        pygame.draw.circle(led_surface, self._color, self._pos, self._radius * 0.5, self._line_width)