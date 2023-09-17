from machine import Pin
import time

trig = Pin(2,Pin.OUT)
echo = Pin(3,Pin.IN)


def distance():
    trig.value(0)
    time.sleep_us(4)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    while echo.value() == 0:
        low = time.ticks_us()
        
    while echo.value() == 1:
        high = time.ticks_us()
        
    print(high - low)

while True:
    distance()
    
    
# GND
# Vcc = Vbus
