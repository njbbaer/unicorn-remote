#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import random


def run():
    m = [[0 for i in range(8)] for i in range(8)]

    while True:
        if 1 in m[-1]:
            top = [0.5 * i for i in m[-1]]
        elif 0.5 in m[-1]:
            top = [0] * 8
        else:
            top = [random.randint(0,1) for i in range(2)] + [0,0,0,0,0,0]
            random.shuffle(top)
            for i in range(len(top)):
                if top[i] == 1 and top[i-1] == 1:
                    top[i] = 0
        m.append(top)
        del m[0]
        for x in range(8):
            for y in range(8):
                h = 0.6
                s = 0.6
                v = m[x][y] * 0.8
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                unicorn.set_pixel(y, x, r, g, b)
        unicorn.show()
        time.sleep(0.05)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--brightness', action='store', dest='brightness', default=0.5, type=float)
    parser.add_argument('-r', '--rotation', action='store', dest='rotation', default=0, type=int)
    params = parser.parse_args()

    unicorn.set_layout(unicorn.AUTO)
    unicorn.brightness(params.brightness)
    unicorn.rotation(params.rotation)

    import sys, os
    file_name =  os.path.basename(sys.argv[0])
    print('Running {}...'.format(file_name))

    run()