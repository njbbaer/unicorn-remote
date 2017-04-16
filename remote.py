from flask import Flask, render_template, request, g
import argparse
import unicornhat as unicorn
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home(brightness=50, program=None):
    if request.method == 'POST':
        brightness = int(request.form['brightness'])
        program = request.form['program']
        unicorn.brightness(brightness/100)
        print('running program', program, 'at', brightness)
            
    return render_template('home.html', brightness=brightness, program=program)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False)
    parser.add_argument('-p', '--port', action='store', dest='port', default=5000, type=int)
    params = parser.parse_args()

    app.run(debug=params.debug, port=params.port, host='0.0.0.0')