from flask import render_template, request, Blueprint
import json

from state import state


index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['POST', 'GET'])
def show():

    if request.method == 'GET':
        return render_template('index.html', 
            program = 'ascii_pic',
            brightness = 0.5,
            rotation = 90,
        )
    
    elif request.method == 'POST':
        params = {
            'brightness': request.form['brightness'],
            'rotation': request.form['rotation'],
        }

        if request.form['submit'] == 'Run':
            state.start_program(request.form['program'], params)
        elif request.form['submit'] == 'Stop':
            state.stop_program()
      
        return render_template('index.html', 
            program = request.form['program'],
            brightness = request.form['brightness'],
            rotation = request.form['rotation'],
        )