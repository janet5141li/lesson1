from gpiozero import LED
from time import sleep

red = LED(27)
red1 = LED(24)

while True:
    red.on()
    red1.off()
    sleep(1)
    red.off()
    red1.on()
    sleep(1)