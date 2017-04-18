from flask import Flask, render_template, request
from flask_restful import Resource, Api
import unicornhat as unicorn
import argparse
import json

app = Flask(__name__)

state = {
    'brightness': 50,
    'program': None,
}

def set_brightness(brightness):
    state['brightness'] = brightness
    unicorn.brightness(brightness/100)

def set_program(program_name):
    state['program'] = program_name

@app.route('/', methods=['POST', 'GET'])
def home(brightness=state['brightness'], 
         program=state['program']):

    if request.method == 'POST':

        if 'brightness' in request.form:
            set_brightness(int(request.form['brightness']))

        if 'program' in request.form:
            set_program(request.form['program'])
            
    return render_template('home.html', brightness=state['brightness'],
                                        program=state['program'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
    parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
    params = parser.parse_args()

    app.run(debug=params.debug, port=params.port, host='0.0.0.0')