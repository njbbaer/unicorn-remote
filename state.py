import unicornhat as unicorn
import subprocess
import sys


PROGRAMS_LIST = ['rainbow', 'snow']


class State:
    ''' Handle Unicorn HAT state'''

    def __init__(self, brightness, program_name):
        self.process = None
        self.set_brightness(brightness)
        self.set_program(program_name)


    def set_brightness(self, brightness):
        self.brightness = brightness
        unicorn.brightness(self.brightness/100)


    def set_program(self, program_name):
        self.program_name = program_name

        # Stop old program
        if self.process is not None:
            self.process.terminate()

        # Start new program
        if self.program_name in PROGRAMS_LIST:
            path = 'programs/' + self.program_name + '.py'
            self.process = subprocess.Popen([sys.executable, path])
            return True
        else:
            return False


# Initialize unicorn state
state = State(brightness=50, program_name=None)