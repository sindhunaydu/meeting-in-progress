# meeting-in-progress
LED meeting indicator

Compoments used - 

  - 8X8 NeoPixel LED Matrix from AliExpress
  - Raspberry Pi 4 
  - Jumper wires
  - 5 push switches from Amazon
  - Solderless breadboard
  - Soldering kit
  
Wiring information - I connected to the following GPIO pins.

  1. 8x8 WS2812B LED Matrix
  
    - DIN -> GPIO18
    - GND and 5V can be connected to corresponding pins in the GPIO

  2. Buttons
  
    - Button 1 OUT -> GPIO 12
    - Button 2 OUT -> GPIO 4
    - Button 3 OUT -> GPIO 11
    - Button 4 OUT -> GPIO 26
    - Button 5 OUT -> GPIO 16
    Each button also had GND connections made to corresponding GND pins in the GPIO

`pinout` - command turned out to be super useful for me to understand the GPIO pin positioning on the RPi

`sudo pip3 install rpi_ws281x` - pip3 for python 3 and rpi_ws281x package for programming the matrix.

Now I was ready to write a simple Python script which would light up the LEDs and change to different states using switches. 

The two Python scripts I wrote are, 

- ledBoardController.py
- buttonController.py

I used different messages and the understanding numbering of LEDs was important,

<img width="233" alt="Screen Shot 2021-01-10 at 3 50 41 PM" src="https://user-images.githubusercontent.com/1637811/104138961-d9235480-535c-11eb-963d-646c36089b47.png">

During the implementation phase, I used the following command to run buttonController.py script and test, 

`sudo python3 buttonController.py`

Once everything was in place, I wanted to use the Pi in headless mode and start the script by SSHing from my personal laptop and running the above command.

`ssh pi@raspberrypi.local
sudo python3 buttonController.py`
