import multiprocessing
import unicornhat
import importlib
import sys
import os


class State:
    ''' Handles the Unicorn HAT state'''

    def __init__(self):
        self.process = None

    def start_program(self, name, params={}):
        self.stop_program()

        if "brightness" in params:
            unicornhat.brightness(float(params["brightness"]))

        if "rotation" in params:
            unicornhat.rotation(int(params["rotation"]))

        program = importlib.import_module("app.programs." + name)
        self.process = multiprocessing.Process(target=program.run, args=(params,))
        self.process.start()

    def stop_program(self):
        if self.process is not None:
            self.process.terminate()
        unicornhat.show()


state = State()