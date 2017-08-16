from time import sleep
from sys import exit

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import unicornhat as unicorn


def run(params):
    if "text" in params:
        text = params["text"]
    else:
        text = "Hello, World!"

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
                    unicorn.set_pixel(h, 6-w, 0, 0, 0)
                else:
                    unicorn.set_pixel(h, 6-w, 255, 0, 0)
        unicorn.show()

    while True:
        step()
        sleep(0.1)