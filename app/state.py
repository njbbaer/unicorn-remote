import multiprocessing
import unicornhathd as unicornhat
import importlib
import sys
import os

import app.programs.hd


class State:
    ''' Handles the Unicorn HAT state'''

    def __init__(self):
        self._process = None

    def start_program(self, name, params={}):
        try:
            program = getattr(app.programs.hd, name)
        except AttributeError:
            raise ProgramNotFound(name)

        self.stop_program()

        if params.get("brightness"):
            unicornhat.brightness(float(params["brightness"]))

        if params.get("rotation"):
            unicornhat.rotation(int(params["rotation"]))

        self._process = multiprocessing.Process(target=program.run, args=(params,))
        self._process.start()

    def stop_program(self):
        if self._process is not None:
            self._process.terminate()
        unicornhat.show()


class ProgramNotFound(Exception):
    pass


state = State()