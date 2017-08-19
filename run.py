import argparse
import os

from app import create_app

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--original', action='store_false', dest='is_hd', default=True)
parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
params = parser.parse_args()

app = create_app(is_hd=params.is_hd)
app.run(debug=params.debug, port=params.port, host='0.0.0.0')