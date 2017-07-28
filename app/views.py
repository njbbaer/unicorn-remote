from flask import render_template, request, Blueprint
import json

from app.state import state


index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['POST', 'GET'])
def show():

    if request.method == 'GET':
        return render_template('index.html', 
            program = 'ascii_text',
            brightness = 0.5,
            rotation = 0,
            text = 'Hello, World!',
        )
    
    elif request.method == 'POST':
        params = {}

        if 'brightness' in request.form:
            params['brightness'] = request.form['brightness']

        if 'rotation' in request.form:
            params['rotation'] = request.form['rotation']

        if 'text' in request.form:
            params['text'] = request.form['text']

        if request.form['submit'] == 'Run':
            state.start_program(request.form['program'], params)
        elif request.form['submit'] == 'Stop':
            state.stop_program()
      
        return render_template('index.html', 
            program = request.form['program'],
            brightness = request.form['brightness'],
            rotation = request.form['rotation'],
            text = request.form['text'],
        )