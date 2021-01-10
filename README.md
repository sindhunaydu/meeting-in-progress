# meeting-in-progress
LED meeting indicator

Tools used - 

  - 8X8 NeoPixel LED Matrix from AliExpress - 
  - Raspberry Pi 4 
  - Jumper wires
  - 5 switches from Amazon - 
  - Soldering kit
  
Wiring information - I connected to the following GPIOs, but it can be connected to any corresponding GPIOs.

  1. 8x8 NeoPixel LED Matrix
  
    - DIN -> GPIO
    - GND -> GND
    - 5v -> 5V

  2. Switches
  
    - IN -> GPIO
    - GND ->

`pinout` - command turned out to be super useful for me to understand the GPIO pin positioning on my RPi 4

`sudo pip3 install rpi_ws281x` - pip3 for python 3 and rpi_ws281x package for programming the matrix I used.

Now we are ready to code a simple Python program to light up the LED matrix and change to different states using switches. 

The two Python scripts I used for this project are, 

- led_test.py
- button_test.py

Finally I executed the following command to run button_test.py and activated the LED meeting-in-progress project, 

`sudo python3 button_test.py`

