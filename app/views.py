from flask import render_template, request, Blueprint
import json

from app.state import state


index = Blueprint('index', __name__, template_folder='templates')
@index.route('/', methods=['GET'])
def show():
    
    if request.method == 'GET':
         return render_template('index.html')