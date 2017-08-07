from flask import request
from flask_restful import Resource, abort

from app.state import state


class PostProgram(Resource):

    def post(self, program_name):
            args = request.args

            try:
                state.start_program(program_name, args)
            except ValueError as e:
                abort(400, error=str(e))