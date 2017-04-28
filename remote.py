from flask import Flask, request
from flask_restful import Api
import argparse
import atexit

from pages import index
from state import state
from api import PostProgram


app = Flask(__name__)
app.register_blueprint(index)


api = Api(app)
api.add_resource(PostProgram, '/api/<string:program_name>')


def exit_handler():
    state.stop_program
atexit.register(exit_handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
    parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
    params = parser.parse_args()

    try:
        app.run(debug=params.debug, port=params.port, host='0.0.0.0')
    finally:
        state.stop_program()