import utime
from machine import I2C, Pin , ADC , Timer
from time import sleep

led = Pin(25,Pin.OUT)
sensor_temp = ADC(4) # 4 numaralı pinde sıcaklık sensörü var
timer = Timer() 
conversion_factor = 3.3 / (65535)

def blink(timer): 
    led.toggle()


def Sıcaklık():
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706)/0.001721
        if temperature < 25:
            timer.init(freq=1,mode=Timer.PERIODIC,callback=blink)
            print("sıcaklık {}".format(temperature))
            temperature = str(temperature)[0:5]
            sleep(1)             
        
Sıcaklık()


