import time
from machine import Pin
import sys

import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd




I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def greeting(text="none"):
    try:
        a = int(text)
        lcd.clear()
        lcd.move_to(4,0)
        lcd.putstr(str(text))
        utime.sleep(2)
        lcd.clear()
    except:
        lcd.clear()
        lcd.move_to(4,0)
        lcd.putstr("hata")
        utime.sleep(2)
        lcd.clear()

while True:
    # read a command from the host
    v = sys.stdin.readline().strip()
    greeting(v)
    
    
        