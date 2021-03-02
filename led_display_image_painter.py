import pygame
from led_display_painter import Painter

class ImagePainter(Painter):
    def __init__(self, image_file):
        Painter.__init__(self)
        self._image = pygame.image.load(image_file)

    def paint(self, led_surface):
        Painter.paint(self, led_surface)

        led_surface.blit(self._image, (0, 0))
