from flask import render_template, request, Blueprint
import json

from state import state

index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['POST', 'GET'])
def show():

    if request.method == 'POST':

        if request.form['submit'] == 'Run':
            params = {
                'brightness': request.form['brightness'],
                'rotation': request.form['rotation'],
            }
            state.set_program(request.form['program'], params)

        elif request.form['submit'] == 'Stop':
            state.stop_program()
            
    return render_template('index.html', 
        brightness = state.get_brightness(),
        rotation = state.get_rotation(),
    )