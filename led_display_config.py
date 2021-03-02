import time
import threading
import configparser

HAS_281x_LIB = True
try:
    from rpi_ws281x import *
except ImportError:
    HAS_281x_LIB = False

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance

class Config(metaclass=SingletonType):
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config_file = "led_display_config.ini"
        self.__config.read(self.__config_file)

        self._win_width = 480
        self._win_height = (16 + 32) * 10 + 60

        self._led_canvas_width = 16 * 10
        self._led_canvas_height = (16 + 32) * 10

        self._led_canvas_pos_x = 30
        self._led_canvas_pos_y = (self._win_height - self._led_canvas_height) // 2

        self._led_col = 16
        self._led_row = 16 + 32

        self._fps = 60

        if self.__config.has_option('led', 'has_led_device'):
            self._has_led_device = True if int(self.__config.get('led', 'has_led_device')) == 1 else False
        else:
            self._has_led_device = False

        self._has_led_device  = self._has_led_device  and HAS_281x_LIB

    @property
    def win_width(self):
        return self._win_width

    @property
    def win_height(self):
        return self._win_height

    @property
    def led_canvas_width(self):
        return self._led_canvas_width

    @property
    def led_canvas_height(self):
        return self._led_canvas_height

    @property
    def led_canvas_pos_x(self):
        return self._led_canvas_pos_x

    @property
    def led_canvas_pos_y(self):
        return self._led_canvas_pos_y

    @property
    def led_row(self):
        return self._led_row

    @property
    def led_col(self):
        return self._led_col

    @property
    def has_led_device(self):
        return self._has_led_device

    @property
    def fps(self):
        return self._fps

    @property
    def win_background_color(self):
        return (80, 80, 80)

    @property
    def highlight_color(self):
        return (255, 0, 0)

    @property
    def button_background_color(self):
        return (0, 0, 0)

    @property
    def button_mouseover_color(self):
        return (50, 64, 50)

    @property
    def button_mousedown_color(self):
        return (90, 100, 90)

    @property
    def button_mousedown_mouseover_color(self):
        return (100, 125, 100)

    @property
    def button_border_color(self):
        return (150, 150, 150)

    @property
    def button_checked_border_color(self):
        return (0, 255, 0)

    @property
    def button_text_color(self):
        return (255, 255, 255)

