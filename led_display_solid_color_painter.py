import pygame
from led_display_painter import Painter

class SolidColorPainter(Painter):
    def __init__(self, color):
        Painter.__init__(self)
        self._color = color

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        pygame.draw.rect(led_surface, self._color, (0, 0, self._config.led_col, self._config.led_row))
