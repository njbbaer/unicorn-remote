#!/usr/bin/env python

from random import randint
import unicornhat as unicorn



def run():
    width,height=unicorn.get_shape()

    while True:
        x = randint(0, (width-1))
        y = randint(0, (height-1))
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()


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