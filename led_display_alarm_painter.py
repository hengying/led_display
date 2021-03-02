import pygame
from led_display_painter import Painter
from led_display_line_particle import LineParticle
from led_display_enum import *

class AlarmPainter(Painter):
    def __init__(self, show_short_lines):
        Painter.__init__(self)
        self._flag = 0
        self._show_short_lines = show_short_lines

    def update(self):
        Painter.update(self)

        c = self._config
        if self.count % 4 == 0:
            self._flag += 1
        if self._flag >= 16:
            self._flag = 0

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        if(self._flag // 8 % 2 == 0):
            pygame.draw.rect(led_surface, (255, 0, 0), (0, 0, 4, 4))
            pygame.draw.rect(led_surface, (0, 0, 255), (12, 0, 4, 4))
            if self._show_short_lines and self.count % 4 == 0 and self._flag %8 == 0:
                self.add_particle(
                    LineParticle(
                        [0, 3],
                        [3, 3],
                        Direction.DOWN,
                        1,
                        (255, 0, 0)))
                self.add_particle(
                    LineParticle(
                        [12, 3],
                        [15, 3],
                        Direction.DOWN,
                        1,
                        (0, 0, 255)))
        else:
            pygame.draw.rect(led_surface, (0, 0, 255), (0, 0, 4, 4))
            pygame.draw.rect(led_surface, (255, 0, 0), (12, 0, 4, 4))
            if self._show_short_lines and self.count % 4 == 0 and self._flag %8 == 0:
                self.add_particle(
                    LineParticle(
                        [0, 3],
                        [3, 3],
                        Direction.DOWN,
                        1,
                        (0, 0, 255)))
                self.add_particle(
                    LineParticle(
                        [12, 3],
                        [15, 3],
                        Direction.DOWN,
                        1,
                        (255, 0, 0)))

        if(self._flag // 8 % 4 == 0):
            pygame.draw.rect(led_surface, (255, 255, 255), (4, 0, 4, 4))
            if self._show_short_lines and self.count % 4 == 0 and self._flag % 8 == 0:
                self.add_particle(
                    LineParticle(
                        [4, 3],
                        [7, 3],
                        Direction.DOWN,
                        1,
                        (255, 255, 255)))

            if(self._flag % 2 == 0):
                pygame.draw.rect(led_surface, (0, 0, 0), (8, 0, 4, 4))
            else:
                pygame.draw.rect(led_surface, (255, 255, 255), (8, 0, 4, 4))

                if self._show_short_lines and self.count % 4 == 0 and self._flag % 2 == 1:
                    self.add_particle(
                        LineParticle(
                            [8, 3],
                            [11, 3],
                            Direction.DOWN,
                            1,
                            (255, 255, 255)))
        else:
            if(self._flag % 2 == 0):
                pygame.draw.rect(led_surface, (0, 0, 0), (4, 0, 4, 4))
            else:
                pygame.draw.rect(led_surface, (255, 255, 255), (4, 0, 4, 4))

                if self._show_short_lines and self.count % 4 == 0 and self._flag % 2 == 1:
                    self.add_particle(
                        LineParticle(
                            [4, 3],
                            [7, 3],
                            Direction.DOWN,
                            1,
                            (255, 255, 255)))

            pygame.draw.rect(led_surface, (255, 255, 255), (8, 0, 4, 4))
            if self._show_short_lines and self.count % 4 == 0 and self._flag % 8 == 0:
                self.add_particle(
                    LineParticle(
                        [8, 3],
                        [11, 3],
                        Direction.DOWN,
                        1,
                        (255, 255, 255)))

        self.paint_particles(led_surface)
