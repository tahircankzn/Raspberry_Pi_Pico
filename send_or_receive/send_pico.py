import os
import utime
from machine import ADC
from machine import Pin, Timer

temp_sensor = ADC(4)
conversion_factor = 3.3 / (65535)
led = Pin(25,Pin.OUT)

def temp1():
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    
    return temperature
    

print("os name : ",os.uname())
uart = machine.UART(0, baudrate=9600)
print("UART info : ",uart)
utime.sleep(3)

while True:
    temp = int(temp1())
    print(temp)
    
    uart.write(str(temp)) 
    #uart.write("Merhaba dünya!")
    #uart.write(f"{str(temp)}99")
    #uart.write(f"{temp}99".encode())
    #led.value(1)
    utime.sleep(2)
    led.value(0)
    #utime.sleep(1)
    
    


