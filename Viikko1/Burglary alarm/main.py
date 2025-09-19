
from machine import Pin
from time import sleep

pir = Pin(28, Pin.IN)

while True:
    if pir.value() == 1:
        print("Motion detected!")
        sleep(2)
    sleep(0.1)
