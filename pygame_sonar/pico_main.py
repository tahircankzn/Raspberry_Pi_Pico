import os
import utime
from machine import ADC
from machine import Pin, Timer, PWM
import time

trig = Pin(2,Pin.OUT)
echo = Pin(3,Pin.IN)

servo = PWM(Pin(15))
servo.freq(50)

temp_sensor = ADC(4)
conversion_factor = 3.3 / (65535)
led = Pin(25,Pin.OUT)

print("os name : ",os.uname())
uart = machine.UART(0, baudrate=9600)
print("UART info : ",uart)
utime.sleep(3)
liste=[]
for i in range(3000,5500,10):
    liste.append(i)

    
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
    if high - low < 1000 :
        return 100
    else:
        return 0

def engine2():
    x = 3000
    mode = 0
    while True:
        if mode == 0:
            for y in range(3000,5500):
                if x > 5500:
                    mode = 1
                    break
                    #x = 3000
                else:
                    x+=10
                    servo.duty_u16(x)
                print(str((int(int(x-3000)/70)+distance())))    
                uart.write(str((int(int(x-3000)/70)+distance()))) 
                utime.sleep(0.01)
        else:
            for y in range(3000,5500):
                if x < 3000:
                    mode = 0
                    break
                    #x = 3000
                else:
                    x-=10
                    servo.duty_u16(x)
                print(str((int(int(x-3000)/70)+distance())))
                uart.write(str((int(int(x-3000)/70)+distance())))
                utime.sleep(0.01) 
    

engine2()


    
    
    



