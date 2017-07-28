from flask import Flask, request
from flask_restful import Api
import atexit

from app.views import index
from app.state import state
from app.api import PostProgram


app = Flask(__name__)
app.register_blueprint(index)

api = Api(app)
api.add_resource(PostProgram, '/api/<string:program_name>')

atexit.register(state.stop_program)