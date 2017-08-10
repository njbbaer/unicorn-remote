import argparse
import os

from app import app


if os.geteuid() != 0:
    raise OSError("Must be run as root")

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
params = parser.parse_args()

app.run(debug=params.debug, port=params.port, host='0.0.0.0')