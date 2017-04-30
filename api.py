from flask import request
from flask_restful import Resource, abort
from state import state


class PostProgram(Resource):

    def post(self, program_name):
            args = request.args

            if 'brigthness' in args:
                if not 0 <= float(args['brightness']) <= 1:
                    abort(404, error="Brigthness must be a float between 0 and 1")

            if 'rotation' in args:
                print(args['rotation'])
                if not int(args['rotation']) in [0, 90, 180, 270]:
                    abort(404, error="Rotation must be 0, 90, 180, or 270 degrees")

            if not state.start_program(program_name, args):
                abort(404, error="The selected program was not found")