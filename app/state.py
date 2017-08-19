import multiprocessing
import unicornhathd as unicornhat
import importlib
import sys
import os

import unicornhat
import unicornhathd
import app.programs.original
import app.programs.hd


class State:
    ''' Handles the Unicorn HAT state'''

    def __init__(self, is_hd=True):
        self._process = None
        self.set_model(is_hd)


    def set_model(self, is_hd):
        if is_hd is True:
            self._unicornhat = unicornhathd
            self._app_programs = app.programs.hd
        else:
            self._unicornhat = unicornhat
            self._app_programs = app.programs.original


    def start_program(self, name, params={}):
        try:
            program = getattr(self._app_programs, name)
        except AttributeError:
            raise ProgramNotFound(name)

        self.stop_program()

        if params.get("brightness") is not None:
            brightness = float(params["brightness"])
            if 0 <= brightness <= 1:
                self._unicornhat.brightness(brightness)
            else:
                raise ValueError("Brightness must be between 0.0 and 1.0")

        if params.get("rotation") is not None:
            rotation = int(params["rotation"])
            if rotation in [0, 90, 180, 270]:
                self._unicornhat.rotation(rotation)
            else:
                raise ValueError("Rotation must be 0, 90, 180 or 270 degrees")

        self._process = multiprocessing.Process(target=program.run, args=(params,))
        self._process.start()


    def stop_program(self):
        if self._process is not None:
            self._process.terminate()
        self._unicornhat.show()


state = State()


class ProgramNotFound(Exception):
    pass