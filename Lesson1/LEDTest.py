from machine import Pin
from time import sleep

myLED = Pin('LED', Pin.OUT)
while True:
    myLED.value(1)
    sleep(.1)
    myLED.value(0)
    sleep(2)
    #toggle()