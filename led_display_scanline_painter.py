import pygame
from led_display_painter import Painter
from led_display_line_particle import LineParticle
from led_display_enum import *

class ScanlinePainter(Painter):
    def __init__(self):
        Painter.__init__(self)

    def update(self):
        Painter.update(self)

        if self.particle_count == 0:
            c = self._config
            self.add_particle(
                LineParticle(
                    [0, 0],
                    [self._config.led_col - 1, 0],
                    Direction.DOWN,
                    1,
                    (0, 255, 0)))

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        self.paint_particles(led_surface)
