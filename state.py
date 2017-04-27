import unicornhat as unicorn
import subprocess
import sys
from threading import Thread

from programs.matrix import run


class State:
    ''' Handle Unicorn HAT state'''

    def __init__(self, params):
        self.program_name = 'None'
        self.process = None
        self.params = params


    def get_program_name(self):
        return self.program_name


    def get_brightness(self):
        return self.params['brightness']


    def get_rotation(self):
        return self.params['rotation']


    def set_program(self, program_name, params):
        self.program_name = program_name
        self.params = params

        self.stop_program()

        # Start new program
        path = 'programs/' + program_name + '.py'
        args = [sys.executable, path]
        for k, v in params.items():
            args.extend(['--' + k, v])
        self.process = subprocess.Popen(args)
        return True


    def stop_program(self):
        if self.process is not None:
            self.process.terminate()
            print("Stopped " + self.program_name)


# Initialize unicorn state
state = State({'brightness': '0.5', 'rotation': '90'})