import multiprocessing
import importlib
import sys
import os


class State:
    ''' Handles the Unicorn HAT state'''

    def __init__(self, is_hd=True):
        self._process = None
        self.set_model(is_hd)


    def set_model(self, is_hd):
        self.is_hd = is_hd
        if self.is_hd is True:
            import unicornhathd
            import app.programs.hd
            self._unicornhat = unicornhathd
            self._app_programs = app.programs.hd.list
        else:
            import unicornhat
            import app.programs.original
            self._unicornhat = unicornhat
            self._app_programs = app.programs.original.list


    def start_program(self, name, params={}):
        program = self._get_program(name)
        self.stop_program()
        self._set_rotation(params)
        self._set_brightness(params)
        self._start_process(program, params)


    def stop_program(self):
        if self._process is not None:
            self._process.terminate()
        self._unicornhat.show()


    def _get_program(self, name):
        try:
            return self._app_programs[name]
        except KeyError:
            raise ProgramNotFound(name)


    def _set_brightness(self, params):
        if params.get("brightness") is not None:
            brightness = float(params["brightness"])
            if 0 <= brightness <= 1:
                self._unicornhat.brightness(brightness)
            else:
                raise ValueError("Brightness must be between 0.0 and 1.0")

    def _set_rotation(self, params):
        if params.get("rotation") is not None:
            rotation = int(params["rotation"])
            if rotation in [0, 90, 180, 270]:
                self._unicornhat.rotation(rotation)
            else:
                raise ValueError("Rotation must be 0, 90, 180 or 270 degrees")

    def _start_process(self, program, params):
        run_program = importlib.import_module(program.location).run
        self._process = multiprocessing.Process(target=run_program, args=(params,))
        self._process.start()


state = State()


class ProgramNotFound(Exception):
    pass
