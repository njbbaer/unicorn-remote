![Unicorn Remote](unicorn-remote-logo.png)

Show off your Unicorn HAT LED matrix by controlling it though a web interface, or automate it with the API.

Available from Pimoroni:  
http://shop.pimoroni.com/products/unicorn-hat

## Setup

Because Unicorn HAT uses the PWM hardware, which is also how your Raspberry Pi generates analog audio, you must disable analog output. In your `/boot/config.txt` comment out the line:
```
#dtparam=audio=on
```

Clone or download the git repository:
```
git clone https://github.com/njbbaer/unicorn-remote.git && cd unicorn-remote
```

Install dependencies:
```
pip3 -r install requirements.txt
```

Start the Unicorn Remote:
```
sudo python3 remote.py
```
`-d`, `--debug` enable debugging mode  
`-p`, `--port` `<port>` set port number (default 5000)

## Web Interface
Visit the Unicorn Remote web interface by directing your browser to your Pi's IP address and specified port.

If running locally, it should be:
```127.0.0.1:5000```

1. Enter the desired LED brightness (between 0 and 1) and display rotation (0, 90, 180, or 270).
2. Choose a program from the dropdown list.
3. Press `Run` to start the program, and `Stop` to end it.

## RESTful API

To control the Unicorn programmatically, use the API by placing a POST request to the webserver.

```
localhost:5000/<program>/?<parameter>=<value>
```
```
localhost:5000/matrix/brightness=0.5&rotation=90
```

## Contribute

Please report bugs and request features as GitHub issues. I welcome all feedback.

Feel free to fork and improve the repository, then submit a pull request.
