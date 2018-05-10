import unicornhathd
import time, colorsys
import math


FLAG = [
    "BWBWBWBWRRRRRRRR",
    "WBWBWBWBWWWWWWWW",
    "BWBWBWBWRRRRRRRR",
    "WBWBWBWBWWWWWWWW",
    "BWBWBWBWRRRRRRRR",
    "WBWBWBWBWWWWWWWW",
    "BWBWBWBWRRRRRRRR",
    "WBWBWBWBWWWWWWWW",
    "RRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWW",
    "RRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWW",
    "RRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWW",
    "RRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWW",
]

def lookup_color(x, y):
    color_letter = FLAG[15-x][15-y]
    if color_letter == "R":
        return (255,0,0)
    elif color_letter == "W":
        return (255,255,255)
    elif color_letter == "B":
        return (0, 0, 255)


def compute_z(x, y, t):
    x = x + t / 20
    y = y + t / 20
    z = math.sin(x + y) + math.cos(x + y)
    z = (z + 2) / 4
    return z


def run(params={}):
    while True:
        for t in range(10000):
            for y in range(16):
                for x in range(16):
                    h = 0.1
                    s = 1.0
                    v = compute_z(x, y, t)
                    rgb = colorsys.hsv_to_rgb(h, s, v)
                    r, g, b = lookup_color(x, y)
                    r = r * v
                    g = g * v
                    b = b * v
                    unicornhathd.set_pixel(x, y, r, g, b)
            unicornhathd.show()
            time.sleep(0.04)


if __name__ == "__main__":
    unicornhathd.rotation(0)
    run()
