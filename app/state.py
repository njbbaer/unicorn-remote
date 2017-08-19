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

        if is_hd is True:
            self._unicornhat = unicornhathd
            self._app_programs = app.programs.hd
        else:
            self._unicornhat = unicornhat
            self. app_programs = app.programs.original


    def start_program(self, name, params={}):
        try:
            program = getattr(self._app_programs, name)
        except AttributeError:
            raise ProgramNotFound(name)

        self.stop_program()

        if params.get("brightness") is not None:
            self._unicornhat.brightness(float(params["brightness"]))

        if params.get("rotation") is not None:
            self._unicornhat.rotation(int(params["rotation"]))

        self._process = multiprocessing.Process(target=program.run, args=(params,))
        self._process.start()

    def stop_program(self):
        if self._process is not None:
            self._process.terminate()
        self._unicornhat.show()


class ProgramNotFound(Exception):
    pass