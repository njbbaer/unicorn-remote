![Unicorn Remote](logo.png)

Unicorn Remote is a Python web application designed to run on a Raspberry Pi with attached Unicorn HAT LED matrix. Users can run animated programs on the HAT from a web interface or with the REST API.

The Unicorn HAT is available from Pimoroni:  
http://shop.pimoroni.com/products/unicorn-hat

I highly recommend this case:  
https://shop.pimoroni.com/products/pibow-for-raspberry-pi-3  
With a diffuser:  
https://shop.pimoroni.com/products/pibow-modification-layers  
Optionally, add a QR code or NFC chip to share the web address.

## Setup

1. Disable analog audio output. Analog audio inteferes with the Unicorn HAT. In your `/boot/config.txt` comment the line:
```
#dtparam=audio=on
```

2. Clone or download the git repository:
```
git clone https://github.com/njbbaer/unicorn-remote.git && cd unicorn-remote
```

3. Install dependencies:
```
python setup.py install
```

4. Start the Unicorn Remote:
```
sudo python run.py
```
*Note:* Must be run with `sudo` or root user

#### Optional Arguments
[`-d`, `--debug`] enable debugging mode  
[`-p`, `--port` `<port>`] set port number (default 5000)

## Web Interface
Visit the web interface by directing a browser to the server's address.
```
http://127.0.0.1:5000
```

* Enter the desired brightness (between 0 and 1) and display rotation (0, 90, 180, or 270).
* Choose a program from the dropdown list.
* Press `Run` to start the program, and `Stop` to end it.

## RESTful API

Control the Unicorn HAT programmatically by placing a POST request to the remote's API.
```
<ip-address>:<port>/api/<program>/?<parameter>=<value>
```
```
POST http://127.0.0.1:5000/api/matrix/?brightness=0.5&rotation=90
```

## Testing
Run the test suite.
```
sudo python -m unittest
```

## Contribute
* **Star this repository** to increase expose.
* Report bugs and request features as GitHub issues.
* Improve the repository and submit a pull request.

