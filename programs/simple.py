#!/usr/bin/env python

import time

import unicornhat as unicorn


def run():
    width,height=unicorn.get_shape()


    for y in range(height):
      for x in range(width):
        unicorn.set_pixel(x,y,255,0,255)
        unicorn.show()
        time.sleep(0.05)

    time.sleep(1)


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