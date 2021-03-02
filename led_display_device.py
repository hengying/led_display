try:
    from rpi_ws281x import *
except ImportError:
    pass

from led_display_config import Config

# LED strip configuration:
LED_COUNT      = 512     # Number of LED pixels.
LED_BRIGHTNESS = 20      # Set to 0 for darkest and 255 for brightest

#======================================
# do not change:
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
#=====================================

class Device():
    def __init__(self):
        self._config = Config()
        self._generate_LED_map()
        self._init_led_strip()

    def _generate_LED_map(self):
        self._led_map = []
        for j in range(self._config.led_row):
            led_row = []

            for i in range(self._config.led_col):
                # -1 means there is no LED pixel
                led_row.append(-1)

            self._led_map.append(led_row)

        #print(self._led_map)

        for j in range(16):
            if j % 2 == 0:
                for i in range(16):
                    self._led_map[j][-i-1] = j * 16 + i
            else:
                for i in range(16):
                    self._led_map[j][i] = j * 16 + i

        for j in range(32):
            if j % 2 == 0:
                for i in range(8):
                    self._led_map[j + 16][-i-5] = 256 + j * 8 + i
            else:
                for i in range(8):
                    self._led_map[j + 16][i+4] = 256 + j * 8 + i

        #print(self._led_map)

    def _get_pixel_index(self, col, row):
        return self._led_map[row][col]

    def show_led(self, surface):
        for i in range(self._config.led_col):
            for j in range(self._config.led_row):
                index = self._get_pixel_index(i, j)
                if index != -1:
                    c = surface.get_at((i, j))
                    self._strip.setPixelColor(index, Color(c[0], c[1], c[2]))

        self._strip.show()

    def _init_led_strip(self):
        self._strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self._strip.begin()

    def clear_leds(self):
        for i in range(16 * 16 + 32 * 8):
            self._strip.setPixelColor(i, Color(0, 0, 0))

        self._strip.show()

