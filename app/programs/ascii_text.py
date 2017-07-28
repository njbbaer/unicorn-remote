#!/usr/bin/env python

from time import sleep
from sys import exit

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import unicornhat as unicorn


def run(text):
    width,height=unicorn.get_shape()

    figletText = figlet_format(text+'  ', "banner", width=1000) # banner font generates text with heigth 7
    textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
    textWidth = len(textMatrix[0]) # the total length of the result from figlet
    global i 
    i = -1

    def step():
        global i
        i = 0 if i>=100*textWidth else i+1 # avoid overflow
        for h in range(height):
            for w in range(width):
                hPos = (i-h) % textWidth
                chr = textMatrix[w][hPos]
                if chr == ' ':
                    unicorn.set_pixel(w, h, 0, 0, 0)
                else:
                    unicorn.set_pixel(w, h, 255, 0, 0)
        unicorn.show()

    while True:
        step()
        sleep(0.1)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--brightness', action='store', dest='brightness', default=0.5, type=float)
    parser.add_argument('-r', '--rotation', action='store', dest='rotation', default=0, type=int)
    parser.add_argument('-t', '--text', action='store', dest='text', type=str)
    params, unknown = parser.parse_known_args()

    print(params)
    
    unicorn.set_layout(unicorn.AUTO)
    unicorn.brightness(params.brightness)
    unicorn.rotation(params.rotation)

    import sys, os
    file_name =  os.path.basename(sys.argv[0])
    print('Running {}...'.format(file_name))

    run(params.text)