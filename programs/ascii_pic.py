#!/usr/bin/env python

from time import sleep
import unicornhat as unicorn


def run():
    width,height=unicorn.get_shape()

    # Every line needs to be exactly 8 characters
    # but you can have as many lines as you like.
    ASCIIPIC = [
         "  X  X  "
        ,"  X  X  "
        ,"        "
        ," X    X "
        ,"  XXXX  "
        ,"        "
        ,"        "
        ,"        "
        ,"  X  X  "
        ,"  X  X  "
        ,"        "
        ,"  XXXX  "
        ," X    X "
        ,"        "
        ,"        "
        ,"        "
        ]
    global i
    i = -1

    def step():
        global i
        i = 0 if i>=100*len(ASCIIPIC) else i+1 # avoid overflow
        for h in range(height):
            for w in range(width):
                hPos = (i+h) % len(ASCIIPIC)
                chr = ASCIIPIC[hPos][w]
                if chr == ' ':
                    unicorn.set_pixel(w, h, 0, 0, 0)
                else:
                    unicorn.set_pixel(w, h, 255, 0, 0)
        unicorn.show()

    while True:
        step()
        sleep(0.2)


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