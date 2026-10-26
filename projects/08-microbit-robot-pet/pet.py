# micro:bit Robot Pet (MicroPython) - python.microbit.org
from microbit import *

display.show(Image.HAPPY)
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    elif button_b.was_pressed():
        display.show(Image.SAD)
    elif accelerometer.was_gesture('shake'):
        display.show(Image.CONFUSED)
        sleep(1000)
        display.show(Image.ASLEEP)
    sleep(100)
