import random
import pygame
from led_display_painter import Painter
from led_display_circle_particle import CircleParticle
from led_display_enum import *
from  led_display_utils import *

class CirclePainter(Painter):
    def __init__(self, probability):
        Painter.__init__(self)
        self._probability = probability
        self._rgb_rotate = RGBRotate()

    def update(self):
        Painter.update(self)


        if random.random() < self._probability:
            self._rgb_rotate.set_hue_rotation(random.uniform(0, 360))

            self.add_particle(
                CircleParticle(
                    [random.randint(0, self._config.led_col - 1), random.randint(0, self._config.led_row - 1)],
                    0.1,
                    (self._rgb_rotate.apply(255, 100, 100)),
                    1))

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        self.paint_particles(led_surface)
