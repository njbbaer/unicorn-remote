from flask import render_template, request, Blueprint
import json

from state import state
from config import programs_list

index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['POST', 'GET'])
def show():

    if request.method == 'POST':
        params = {
            'brightness': request.form['brightness'],
            'rotation': request.form['rotation'],
        }
        state.set_program(request.form['program'], params)
            
    return render_template('index.html', 
        brightness = state.get_brightness(),
        rotation = state.get_rotation(),
    )