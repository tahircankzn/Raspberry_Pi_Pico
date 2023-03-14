
import select
import sys
import machine
import utime
import time         #time library for sleep

from machine import Pin
led = Pin(25, Pin.OUT)
while True:
    
    if select.select([sys.stdin],[],[],0)[0]:
        ch = sys.stdin.read(2) #read one byte
        print(f"{ch}")
        if ch == "ld":
            led.on()
        elif ch == "lu":
            led.off()
        elif ch == "rd":
            led.on()
        elif ch == "ru":
            led.off()