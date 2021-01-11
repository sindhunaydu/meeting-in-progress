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

The numbering of LEDs (took a while to figure that out),

<img width="233" alt="Screen Shot 2021-01-10 at 3 50 41 PM" src="https://user-images.githubusercontent.com/1637811/104138961-d9235480-535c-11eb-963d-646c36089b47.png">

* add table

Finally I executed the following command to run button_test.py and activated the LED meeting-in-progress project, 

`sudo python3 button_test.py`

