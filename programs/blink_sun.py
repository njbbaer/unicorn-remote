#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np


def run():
    def make_gaussian(fwhm):
        x = np.arange(0, 8, 1, float)
        y = x[:, np.newaxis]
        x0, y0 = 3.5, 3.5
        fwhm = fwhm
        gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
        return gauss


    fwhm = 0
    while True:
        if fwhm == 0: reverse = False
        if fwhm == 9: reverse = True
        if not reverse:
            fwhm += 1
        else:
            fwhm -= 1


        gauss = make_gaussian(fwhm)
        for y in range(8):
            for x in range(8):
                h = 0.1
                s = 1.0
                v = gauss[x,y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()
        time.sleep(0.05)


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