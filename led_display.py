import os
import sys
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from led_display_config import Config
from led_display_button import Button

from led_display_device import Device

from led_display_solid_color_painter import SolidColorPainter
from led_display_checkbox_painter import CheckBoxPainter
from led_display_scanline_painter import ScanlinePainter
from led_display_alarm_painter import AlarmPainter
from led_display_scroll_text_painter import ScrollTextPainter
from led_display_circle_painter import CirclePainter
from led_display_image_painter import ImagePainter

BLACK = (0, 0, 0)

class LEDDisplay():
    def __init__(self):
        pygame.init()
        self._config = Config()
        self._surface = pygame.display.set_mode((self._config.win_width, self._config.win_height))
        self._clock = pygame.time.Clock()
        self.__font = pygame.font.Font('fonts/uni_dzh.ttf', 24)
        self.__led_font = pygame.font.Font('fonts/uni_dzh.ttf', 16)
        self._led_surface = pygame.Surface((self._config.led_col, self._config.led_row))
        self._buttons = []
        self._painters = []
        self.create_buttons()

        if self._config.has_led_device:
            self._device = Device()
        else:
            self._device = None

        self.black_painter()

    def run(self):
        try:
            while True:
                # 应该有个循环，处理所有的事件
                # while poll() != pygame.NOEVENT:
                e = pygame.event.poll()
                if e.type == pygame.QUIT:
                    raise StopIteration
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down(e.pos)

                if e.type == pygame.MOUSEMOTION:
                    self.mouse_move(e.pos)

                if e.type == pygame.MOUSEBUTTONUP:
                    self.mouse_up(e.pos)

                if e.type == pygame.KEYDOWN:
                    self.key_down(e.key)

                self.update()

                self.paint()

                self._clock.tick(self._config.fps)
                pygame.display.flip()

        except StopIteration:
            self.quit()
        except KeyboardInterrupt:
            self.quit()

    def update(self):
        for painter in (self._painters):
            painter.update()

    def paint(self):
        c = self._config
        pygame.draw.rect(self._surface, c.win_background_color,
                         (0, 0, c.win_width, c.win_height))

        for painter in (self._painters):
            painter.paint(self._led_surface)

        if self._device is not None:
            self._device.show_led(self._led_surface)

        # hide no display part
        pygame.draw.rect(self._led_surface, (0, 0, 0), (0, 16, 4, 32))
        pygame.draw.rect(self._led_surface, (0, 0, 0), (12, 16, 4, 32))

        led_image = pygame.transform.scale(self._led_surface,
                                              (c.led_canvas_width, c.led_canvas_height))

        self._surface.blit(led_image,
                               (c.led_canvas_pos_x, c.led_canvas_pos_y))

        self.show_fps()

        for button in self._buttons:
            button.paint()

    def mouse_down(self, pos):
        for button in self._buttons:
            if button.mouse_down(pos):
                return True
        return False

    def mouse_move(self, pos):
        for button in self._buttons:
            if button.mouse_move(pos):
                return True
        return False

    def mouse_up(self, pos):
        for button in self._buttons:
            if button.mouse_up(pos):
                return True
        return False

    def key_down(self, key):
        for button in self._buttons:
            if button.key_down(key):
                return True
        return False

    def quit(self):
        if self._device is not None:
            print("Clearing LEDs...")
            self._device.clear_leds()

        pygame.quit()
        sys.exit()

    def show_fps(self):
        text_surface = self.__font.render(str(int(self._clock.get_fps())), False, (125, 200, 125))
        self._surface.blit(text_surface, (self._config.win_width - 35, self._config.win_height - 30))

    @property
    def font(self):
        return self.__font

    @property
    def led_font(self):
        return self.__led_font

    def create_buttons(self):
        button_step_y = 40
        y = 30
        self._quit_button = Button(self, self._surface, (230, y, 100, 35),
                                   '退出', self.quit)
        self._buttons.append(self._quit_button)
        y += button_step_y

        self._black_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                   '黑', self.black_painter)
        self._buttons.append(self._black_painter_button)
        y += button_step_y

        self._checkbox_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                   '棋盘格', self.checkbox_painter)
        self._buttons.append(self._checkbox_painter_button)
        y += button_step_y

        self._scanline_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                               '扫描线', self.scanline_painter)
        self._buttons.append(self._scanline_painter_button)
        y += button_step_y

        self._alarm_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                               '警报', self.alarm_painter)
        self._buttons.append(self._alarm_painter_button)
        y += button_step_y

        self._happy_new_year_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                               '新年快乐', self.happy_new_year_painter)
        self._buttons.append(self._happy_new_year_painter_button)
        y += button_step_y

        self._circle_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                               '水波纹', self.circle_painter)
        self._buttons.append(self._circle_painter_button)
        y += button_step_y

        self._image_painter_button = Button(self, self._surface, (230, y, 100, 35),
                                               '图像', self.image_painter)
        self._buttons.append(self._image_painter_button)
        y += button_step_y


    def uncheck_all_buttons(self):
        for button in self._buttons:
            button.is_checked = False

    def _clear_all_painters(self):
        self._painters.clear()

    def _add_painter(self, painter):
        painter.start()
        self._painters.append(painter)

    def black_painter(self):
        self._clear_all_painters()
        self._add_painter(SolidColorPainter(BLACK))

        self.uncheck_all_buttons()
        self._black_painter_button.is_checked = True

    def checkbox_painter(self):
        self._clear_all_painters()
        self._add_painter(CheckBoxPainter())

        self.uncheck_all_buttons()
        self._checkbox_painter_button.is_checked = True

    def scanline_painter(self):
        self._clear_all_painters()
        self._add_painter(SolidColorPainter(BLACK))
        self._add_painter(ScanlinePainter())

        self.uncheck_all_buttons()
        self._scanline_painter_button.is_checked = True

    def alarm_painter(self):
        self._clear_all_painters()
        self._add_painter(SolidColorPainter(BLACK))
        self._add_painter(AlarmPainter(True))

        self.uncheck_all_buttons()
        self._alarm_painter_button.is_checked = True

    def happy_new_year_painter(self):
        self._clear_all_painters()
        self._add_painter(SolidColorPainter(BLACK))
        self._add_painter(ScrollTextPainter(self.__led_font, '新年快乐！', (255, 0, 0), 1))
        self._add_painter(ScrollTextPainter(self.__led_font, '新年快乐！', (255, 64, 0), 0))

        self.uncheck_all_buttons()
        self._happy_new_year_painter_button.is_checked = True

    def circle_painter(self):
        self._clear_all_painters()
        self._add_painter(SolidColorPainter(BLACK))
        self._add_painter(CirclePainter(0.07))

        self.uncheck_all_buttons()
        self._circle_painter_button.is_checked = True

    def image_painter(self):
        self._clear_all_painters()
        self._add_painter(ImagePainter('images/pony.png'))

        self.uncheck_all_buttons()
        self._circle_painter_button.is_checked = True


if __name__ == '__main__':
    app = LEDDisplay()
    app.run()
    # pygame.quit()
