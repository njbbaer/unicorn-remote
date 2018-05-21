from flask import request
from flask_restful import Resource, abort, reqparse

from app import state
from app.state import ProgramNotFound


class SetProgram(Resource):

    def put(self, program):
        parser = reqparse.RequestParser()
        parser.add_argument('brightness', type=float)
        parser.add_argument('rotation', type=int)
        args = parser.parse_args()

        try:
            state.start_program(program, args)
        except ProgramNotFound as e:
            abort(404, error="Program '{}' not found".format(e))
        except ValueError as e:
            abort(400, error=str(e))
        return {"success": "Program '{}' started".format(program)}


class StopProgram(Resource):

    def put(self):
        state.stop_program()
        return {"success": "Program stopped"}
