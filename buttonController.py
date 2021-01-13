from time import sleep
from gpiozero import Button
import ledBoardController

mic_button = Button(12)
audio_button = Button(4)
video_button = Button(11)
dnd_button = Button(26)
off_button = Button(16)

def led_state_1():
    ledBoardController.led_off()
    ledBoardController.led_mic_on()
    
def led_state_2():
    ledBoardController.led_off()
    ledBoardController.led_audio_on()

def led_state_3():
    ledBoardController.led_off()
    ledBoardController.led_video_on()

def led_state_4():
    ledBoardController.led_off()
    ledBoardController.led_dnd()

def led_state_5():
    ledBoardController.led_off()

mic_button.when_activated = led_state_1
audio_button.when_activated = led_state_2
video_button.when_activated = led_state_3
dnd_button.when_activated = led_state_4
off_button.when_activated = led_state_5

if __name__ == '__main__':
    while True:
        sleep(1)
