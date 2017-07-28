import subprocess
import sys
import os


class State:
    ''' Handles the Unicorn HAT state'''

    def __init__(self):
        self.process = None

    def start_program(self, program_name, params=None):

        # Stop old program
        if self.process is not None:
            self.process.terminate()

        # Start new program
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path + '/programs/' + program_name + '.py'

        if os.path.isfile(path):
            args = [sys.executable, path]
            if params is not None:
                for k, v in params.items():
                    args.extend(['--' + k, v])
            self.process = subprocess.Popen(args)
            return True
        else:
            return False

    def stop_program(self):
        self.start_program('stop')


# Initialize unicorn state
state = State()