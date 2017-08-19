![Unicorn Remote](logo.png)

Unicorn Remote is a Python web application designed to run animated programs on a Raspberry Pi with attached Unicorn HAT LED matrix. It can be controlled from both a web interface and RESTful API.

Unicorn Remote supports both the new Unicorn HAT HD 16x16 and original Unicorn HAT 8x8.

The Unicorn HAT HD is available from Pimoroni:  
https://shop.pimoroni.com/products/unicorn-hat-hd


## Setup
1. Clone or download the git repository:
```
git clone https://github.com/njbbaer/unicorn-remote.git && cd unicorn-remote
```

2. Install dependencies:
```
sudo pip3 install -r requirements.txt
```

3. Start the Unicorn Remote:
```
sudo python3 run.py
```
*Note:* Must be run as root


#### Optional Arguments
`-o` `--original` use original 8x8 unicorn hat  
`-d` `--debug` enable Flask debugging mode  
`-p` `--port` `<port>` set port number (default 5000)



## Web Interface
Visit the web interface by directing a browser to the server's address.
```
http://127.0.0.1:5000
```

* Choose a program from the dropdown list.
* Select the desired brightness and display rotation.
* Press `Run` to start the program, and `Stop` to end it.


## RESTful API
Start a program by placing a PUT request:
```
PUT /api/program/<program_name>
```
* All programs use the optional query parameters `brightness` and `rotatation`. Some take additional parameters (ex. `ascii_text` requires a value for `text`)

Stop the currently running program:
```
DELETE /api/program
```


## Testing
Run the test suite.
```
sudo python3 -m unittest
```


## Contribute
* **Star this repository** to show your interest in this project.
* Give feedback, report bugs, and request features as GitHub issues.
* Improve the repository and submit a pull request.

