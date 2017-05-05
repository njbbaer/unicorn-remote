![Unicorn Remote](unicorn-remote-logo.png)

Unicorn Remote is a Python web application designed to run on a Raspberry Pi with an attached Unicorn HAT LED matrix. Users can run animated programs on the HAT from a web interface or with the REST API.

By default it comes set up with many programs. Some modified from other Unicorn HAT open-source projects. Developers are encouraged to add their own programs, but there is not yet an official way to do so.

The Unicorn Hat is available from Pimoroni:  
http://shop.pimoroni.com/products/unicorn-hat

I also highly recommend this case:  
https://shop.pimoroni.com/products/pibow-for-raspberry-pi-3  
With a diffuser plate:  
https://shop.pimoroni.com/products/pibow-modification-layers  
Optionally add an QR code or NFC chip to share the web address publicly.

This is an independent, open-source project not affiliated with Pimoroni. Primarily developed by Nathaniel Baer.

## Setup

1. Disable analog audio output, because the Raspberry Pi's analog audio generation inteferes with the Unicorn HAT. In your `/boot/config.txt` comment out the line:
```
#dtparam=audio=on
```

2. Clone or download the git repository:
```
git clone https://github.com/njbbaer/unicorn-remote.git && cd unicorn-remote
```

3. Install dependencies:
```
pip3 -r install requirements.txt
```

4. Start the Unicorn Remote:
```
sudo python3 remote.py
```
Note: Must be run with `sudo` or root user

#### Optional Arguments
`-d`, `--debug` enable debugging mode  
`-p`, `--port` `<port>` set port number (default 5000)

## Web Interface
Visit the Unicorn Remote web interface by directing a browser to the pi's network IP address, and the server's port.
```
<ip-address>:<port>
127.0.0.1:5000
```

* Enter the desired LED brightness (between 0 and 1) and display rotation (0, 90, 180, or 270).
* Choose a program from the dropdown list.
* Press `Run` to start the program, and `Stop` to end it.

## RESTful API

To control the Unicorn programmatically, use the API by placing a POST request to the web server.

```
<ip-address>:<port>/<program>/?<parameter1>=<value1>
```
```
127.0.0.1:5000/matrix/brightness=0.5&rotation=90
```

## Contribute

Please report bugs and request features as GitHub issues.

Feel free to fork and improve the repository, then contribute back by submitting a pull request.

