from flask import request
from flask_restful import Resource, abort

from app.state import state, ProgramNotFound


class SetProgram(Resource):

    def put(self, program_name):
            args = request.args

            try:
                state.start_program(program_name, args)
            except ProgramNotFound as e:
                abort(404, error="Program '{}' not found.".format(e))
            except ValueError as e:
                abort(400, error=str(e))


class StopProgram(Resource):

    def delete(self):
        state.stop_program()