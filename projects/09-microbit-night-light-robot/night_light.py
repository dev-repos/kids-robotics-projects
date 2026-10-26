# micro:bit Night-Light Robot (MicroPython)
from microbit import *

while True:
    light = display.read_light_level()   # 0 = dark ... 255 = bright
    if light < 60:
        display.show(Image('99999:99999:99999:99999:99999'))
    else:
        display.clear()
    sleep(200)
