from flask import Flask, render_template, request
from flask_restful import Resource, Api, abort
import unicornhat as unicorn
import argparse
import json
import subprocess
import sys

PROGRAMS_LIST = ['rainbow', 'snow']

app = Flask(__name__)
api = Api(app)


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


@app.route('/', methods=['POST', 'GET'])
def index(brightness=state.brightness, 
         program=state.program_name):

    if request.method == 'POST':

        if 'brightness' in request.form:
            state.set_brightness(int(request.form['brightness']))

        if 'program' in request.form:
            state.set_program(request.form['program'])
            
    return render_template('index.html', brightness=state.brightness,
                                        program_name=state.program_name)


class BrightnessPut(Resource):
    def put(self, level):
        level_int = int(level)
        if level_int >= 0 and level_int <= 100:
            state.set_brightness(level_int)
            return {'brightness': state.brightness}
        else:
            abort(404, message="Brigthness must be an integer between 0 and 100")

class ProgramPut(Resource):
    def put(self, name):
        if state.set_program(name):
            return {'program': state.program_name}
        else:
            abort(404, message="Program {} doesn't exist".format(name))

class BrightnessGet(Resource):
    def get(self):
        return {'brightness': state.brightness}

class ProgramGet(Resource):
    def get(self):
        return {'program': state.program_name}

api.add_resource(BrightnessPut, '/api/brightness/<level>')
api.add_resource(BrightnessGet, '/api/brightness')
api.add_resource(ProgramPut, '/api/program/<name>')
api.add_resource(ProgramGet, '/api/program')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
    parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
    params = parser.parse_args()

    app.run(debug=params.debug, port=params.port, host='0.0.0.0')