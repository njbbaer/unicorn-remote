#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import math


def run():
    def compute_z(x, y, t, pattern):
        x = x + t
        y = y + t
        if pattern == 'parallel':
            z = math.sin(x) + math.cos(x)
            z = (z + 2) / 4
        elif pattern == 'diagonal':
            z = math.sin(x + y) + math.cos(x + y)
            z = (z + 2) / 4
        elif pattern == 'crisscross':
            z = math.sin(x) + math.cos(y)
            z = (z + 2) / 4
        return z

    patterns = ['parallel', 'diagonal', 'crisscross']

    while True:
        for pattern in patterns:
            for t in range(100):
                for y in range(8):
                    for x in range(8):
                        h = 0.1
                        s = 1.0
                        v = compute_z(x, y, t, pattern)
                        rgb = colorsys.hsv_to_rgb(h, s, v)
                        r = int(rgb[0]*255.0)
                        g = int(rgb[1]*255.0)
                        b = int(rgb[2]*255.0)
                        unicorn.set_pixel(x, y, r, g, b)
                unicorn.show()
                time.sleep(0.08)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--brightness', action='store', dest='brightness', default=0.5, type=float)
    parser.add_argument('-r', '--rotation', action='store', dest='rotation', default=0, type=int)
    params, unknown = parser.parse_known_args()

    unicorn.set_layout(unicorn.AUTO)
    unicorn.brightness(params.brightness)
    unicorn.rotation(params.rotation)

    import sys, os
    file_name =  os.path.basename(sys.argv[0])
    print('Running {}...'.format(file_name))

    run()