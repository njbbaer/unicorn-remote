import colorsys
import time
from sys import exit
import unicornhat as unicorn
import random


def run(params):
    width,height=unicorn.get_shape()


    while True:
        rand_mat = [[random.random() for i in range(width)] for j in range(height)]
        for y in range(height):
            for x in range(width):
                h = 0.1 * rand_mat[x][y]
                s = 0.8
                v = rand_mat[x][y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()
        time.sleep(0.02)