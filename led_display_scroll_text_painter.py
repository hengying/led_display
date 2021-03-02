from led_display_config import Config
from led_display_painter import Painter

class ScrollTextPainter(Painter):
    def __init__(self, font, text, color, x_bias):
        Painter.__init__(self)
        self._font = font
        self._text = text
        self._color = color
        self._text_surface = self._font.render(self._text, False, self._color)
        self._text_rect = self._text_surface.get_rect()
        self._config = Config()
        self._pos_x = self._config.led_col
        self._x_bias = x_bias

    def update(self):
        Painter.update(self)

        if self.count % 3 == 0:
            self._pos_x -= 1
        if self._pos_x + self._text_rect[2] < 0:
            self._pos_x = self._config.led_col

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        # 不知为什么，在 iMac 上是 80x16，在Pi上是80x22
        if self._text_rect[3] == 16:
            led_surface.blit(self._text_surface, (self._pos_x + self._x_bias, 0))
        else:
            led_surface.blit(self._text_surface, (self._pos_x + self._x_bias, -2))





