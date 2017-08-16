from random import randint
import unicornhat as unicorn



def run(params):
    width,height=unicorn.get_shape()

    while True:
        x = randint(0, (width-1))
        y = randint(0, (height-1))
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()