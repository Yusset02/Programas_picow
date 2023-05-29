from machine import Pin
from time import sleep

led_obj = machine.Pin('LED',Pin.OUT)
while True:
    led_obj.on()
    sleep(0.5)
    led_obj.off()
    sleep(0.5)
