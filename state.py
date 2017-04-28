import unicornhat as unicorn
import subprocess
import sys
import os
from threading import Thread

from programs.matrix import run


class State:
    ''' Handle Unicorn HAT state'''

    def __init__(self):
        self.process = None


    def set_program(self, program_name, params):
        self.program_name = program_name

        self.stop_program()

        # Start new program
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path + '/programs/' + program_name + '.py'
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
state = State()