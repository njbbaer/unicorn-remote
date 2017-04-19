from flask import render_template, request, Blueprint
from state import state

index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['POST', 'GET'])
def show(brightness=state.brightness, 
         program=state.program_name):

    if request.method == 'POST':

        if 'brightness' in request.form:
            state.set_brightness(int(request.form['brightness']))

        if 'program' in request.form:
            state.set_program(request.form['program'])
            
    return render_template('index.html', brightness=state.brightness,
                                        program_name=state.program_name)