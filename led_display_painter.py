
from led_display_config import Config

class Painter():
    def __init__(self):
        self._config = Config()
        self._count = 0
        self._particles = []

    def add_particle(self, particle):
        self._particles.append(particle)

    def start(self):
        self._count = 0

    def update(self):
        self._count += 1

        for particle in self._particles:
            particle.update()

        self._particles = [p for p in self._particles if p.is_complete == False]

    def paint(self, led_surface):
        pass

    def paint_particles(self, led_surface):
        for particle in self._particles:
            particle.paint(led_surface)

    @property
    def count(self):
        return self._count

    def _reset_count(self):
        self._count = 0

    @property
    def particle_count(self):
        return len(self._particles)