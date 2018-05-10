from flask import render_template, request, Blueprint
from collections import namedtuple

from app.state import state
import app.programs.hd
import app.programs.original


ListItem = namedtuple("Button", "key title")

hd_programs_list = []
for key, program in sorted(app.programs.hd.list.items()):
    hd_programs_list.append(ListItem(key, program.title))

original_programs_list = []
for key, program in sorted(app.programs.original.list.items()):
    original_programs_list.append(ListItem(key, program.title))


index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['GET'])
def show():

    if request.method == 'GET':
        if state.is_hd is True:
            programs_list = hd_programs_list
        else:
            programs_list = original_programs_list
        return render_template('index.html', programs_list=programs_list)
