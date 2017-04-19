from flask import Flask
from flask_restful import Api
import argparse

from pages import index
import api as api_resources


app = Flask(__name__)
app.register_blueprint(index)

api = Api(app)
api.add_resource(api_resources.BrightnessPut, '/api/brightness/<level>')
api.add_resource(api_resources.BrightnessGet, '/api/brightness')
api.add_resource(api_resources.ProgramPut, '/api/program/<name>')
api.add_resource(api_resources.ProgramGet, '/api/program')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
    parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
    params = parser.parse_args()

    app.run(debug=params.debug, port=params.port, host='0.0.0.0')