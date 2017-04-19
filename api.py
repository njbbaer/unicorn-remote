from flask_restful import Resource, abort
from state import state


class BrightnessPut(Resource):
    def put(self, level):
        level_int = int(level)
        if level_int >= 0 and level_int <= 100:
            state.set_brightness(level_int)
            return {'brightness': state.brightness}
        else:
            abort(404, message="Brigthness must be an integer between 0 and 100")


class ProgramPut(Resource):
    def put(self, name):
        if state.set_program(name):
            return {'program': state.program_name}
        else:
            abort(404, message="Program {} doesn't exist".format(name))


class BrightnessGet(Resource):
    def get(self):
        return {'brightness': state.brightness}


class ProgramGet(Resource):
    def get(self):
        return {'program': state.program_name}
