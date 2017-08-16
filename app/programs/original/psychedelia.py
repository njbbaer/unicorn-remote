import unicornhat as unicorn
import time, colorsys
import math


def run(params):
    def compute_z(x, y, t):
        x = x + t
        y = y + t
        h, w = 2, 2
        z = (128.0 + (128.0 * math.sin(x / 16.0)) + 128.0 + (128.0 * math.sin(y / 32.0)) \
        + 128.0 + (128.0 * math.sin(math.sqrt((x - w / 2.0) * (x - w / 2.0) + (y - h / 2.0) * (y - h / 2.0)) / 8.0)) \
        + 128.0 + (128.0 * math.sin(math.sqrt(x * x + y * y) / 8.0))) % 255 / 255
        return z

    t = 0
    while True:
        for y in range(8):
            for x in range(8):
                h = compute_z(x, y, t)
                s = 1.0
                v = 0.4
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()
        time.sleep(0.05)
        t += 1