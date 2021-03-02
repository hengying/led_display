from led_display_config import Config

class Particle():
    def __init__(self):
        self._is_complete = False
        self._config = Config()
        self._count = 0

    def update(self):
        self._count += 1

    def paint(self, led_surface):
        pass

    @property
    def is_complete(self):
        return self._is_complete

