from flask import request
from flask_restful import Resource, abort
from state import state

class PostProgram(Resource):

    def post(self, program_name):

            # Validate arguments
            if 'brigthness' in request.args:
                if not 0 <= float(request.args['brightness']) <= 1:
                    abort(404, error="Brigthness must be a float between 0 and 1")
            if 'rotation' in request.args:
                if not int(request.args['rotation']) in [0, 90, 180, 270]:
                    abort(404, error="Rotation must be 0, 90, 180, or 270 degrees")

            state.set_program(program_name, request.args)
