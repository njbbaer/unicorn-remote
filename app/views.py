from flask import render_template, request, Blueprint
import json

from app.state import state

HD_PROGRAMS_LIST = [
    ["candle",      "Candle"],
    ["demo",        "Demo"],
    ["forest_fire", "Forest Fire"],
    ["game_of_life","Game of Life"],
    ["rainbow",     "Rainbow"],
    ["stars",       "Stars"], 
    ["trig",        "Trig"]
]

ORIGINAL_PROGRAMS_LIST = [
    ["ascii_text",      "ASCII Text"],
    ["cheertree",       "Cheertree"],
    ["cross",           "Cross"],
    ["demo",            "Demo"],
    ["dna",             "DNA"],
    ["game_of_life",    "Game of Life"],
    ["matrix",          "Matrix"],
    ["psychedelia",     "Psychedelia"],
    ["rain",            "Rain"],
    ["rainbow",         "Rainbow"],
    ["random_blinky",   "Random Blinky"],
    ["random_sparkles", "Random Sparkles"],
    ["simple",          "Simple"],
    ["snow",            "Snow"],
    ["trig",            "Trig"],
]


index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['GET'])
def show():
    
    if request.method == 'GET':
        if state.is_hd is True:
            programs_list = HD_PROGRAMS_LIST
        else:
            programs_list = ORIGINAL_PROGRAMS_LIST
        return render_template('index.html', programs_list=programs_list)