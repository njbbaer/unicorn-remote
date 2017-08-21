#!/usr/bin/env python

'''Unicorn HAT HD: Show a PNG image!

This basic example shows use of the Python Pillow library:

sudo pip-3.2 install pillow # or sudo pip install pillow

The tiny 16x16 bosses in lofi.png are from Oddball: http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License.

Press Ctrl+C to exit!

'''

import signal
import time
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd as unicorn


width, height = unicorn.get_shape()

img = Image.open('app/programs/hd/assets/solomon.png')

def run(params):
    while True:
        for o_y in range(int(img.size[1]/height)):
            for o_x in range(int(img.size[0]/width)):

                valid = False
                for y in range(height):
                    for x in range(width):
                    
                        pixel = img.getpixel(((o_x*width)+y,(o_y*height)+x))
                        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicorn.set_pixel(15-x, y, r, g, b)
                if valid:
                    unicorn.show()
                    time.sleep(0.1)