from flask import Flask, request
from flask_restful import Api
import atexit

from app.state import state
from app.views import index
from app.api import SetProgram, StopProgram


def create_app(is_hd=True):
    state.set_model(is_hd)

    app = Flask(__name__)
    app.register_blueprint(index)

    app.config['ERROR_404_HELP'] = False

    api = Api(app)
    api.add_resource(SetProgram, '/api/program/<string:program>')
    api.add_resource(StopProgram, '/api/program')

    atexit.register(state.stop_program)

    return app
