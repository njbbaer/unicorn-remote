#!/usr/bin/env python

import time
from random import randint
import unicornhat as unicorn


def run():
    wrd_rgb = [[154, 173, 154], [0, 255, 0], [0, 200, 0], [0, 162, 0], [0, 145, 0], [0, 96, 0], [0, 74, 0], [0, 0, 0,]]

    clock = 0

    blue_pilled_population = [[randint(0,7), 7]]
    while True:
        for person in blue_pilled_population:
            y = person[1]
            for rgb in wrd_rgb:
                if (y <= 7) and (y >= 0):
                    unicorn.set_pixel(person[0], y, rgb[0], rgb[1], rgb[2])
                y += 1
            person[1] -= 1
        unicorn.show()
        time.sleep(0.1)
        clock += 1
        if clock % 5 == 0:
            blue_pilled_population.append([randint(0,7), 7])
        if clock % 7 == 0:
            blue_pilled_population.append([randint(0,7), 7])
        while len(blue_pilled_population) > 100:
            blue_pilled_population.pop(0)


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