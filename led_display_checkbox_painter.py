import pygame

from led_display_painter import Painter

class CheckBoxPainter(Painter):
    def __init__(self):
        Painter.__init__(self)
        self._flag = 0
        self._checkbox_surface = pygame.Surface((self._config.led_col + 1, self._config.led_row + 1))
        for i in range(self._config.led_canvas_width):
            for j in range(self._config.led_canvas_height):
                if (i + j) % 2 == 0:
                    self._checkbox_surface.set_at((i, j), (0, 255, 0))

    def update(self):
        Painter.update(self)

        if self.count >= self._config.fps:
            self._flag = 1 - self._flag
            self._reset_count()

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        led_surface.blit(self._checkbox_surface, (0, 0),
                         area = (self._flag, 0,
                          self._config.led_col, self._config.led_row))

