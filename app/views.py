from flask import render_template, request, Blueprint
import json

from app.state import state

PROGRAMS_LIST = [
    ["candle",      "Candle"],
    ["demo",        "Demo"],
    ["forest_fire", "Forest Fire"],
    ["game_of_life","Game of Life"],
    ["rainbow",     "Rainbow"],
    ["stars",       "Stars"]
]

# PROGRAMS_LIST = [
#     ["ascii_text",      "ASCII Text"],
#     ["cheertree",       "Cheertree"],
#     ["cross",           "Cross"],
#     ["demo",            "Demo"],
#     ["dna",             "DNA"],
#     ["game_of_life",    "Game of Life"],
#     ["matrix",          "Matrix"],
#     ["psychedelia",     "Psychedelia"],
#     ["rain",            "Rain"],
#     ["rainbow",         "Rainbow"],
#     ["random_blinky",   "Random Blinky"],
#     ["random_sparkles", "Random Sparkles"],
#     ["simple",          "Simple"],
#     ["snow",            "Snow"],
#     ["trig",            "Trig"],
# ]


index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['GET'])
def show():
    
    if request.method == 'GET':
         return render_template('index.html', programs_list=PROGRAMS_LIST)