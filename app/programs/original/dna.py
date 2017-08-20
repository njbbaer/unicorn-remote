from time import sleep
import unicornhat as unicorn


def run(params):
    width,height=unicorn.get_shape()

    # Every line needs to be exactly 8 characters
    # but you can have as many lines as you like.
    ASCIIPIC = [
         "1     2 "
        ," 1     2"
        ,"  1   2 "
        ,"   1 2  "
        ,"    1   "
        ,"   2 1  "
        ,"  2   1 "
        ," 2     1"
        ,"2     1 "
        ," 2   1  "
        ,"  2 1   "
        ,"   2    "
        ,"  1 2   "
        ," 1   2  "
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
                if chr == '1':
                    unicorn.set_pixel(w, h, 255, 255, 255)
                elif chr == '2':
                    unicorn.set_pixel(w, h, 0, 0, 255)
                else:
                    unicorn.set_pixel(w, h, 0, 0, 0)
        unicorn.show()

    while True:
        step()
        sleep(0.1)