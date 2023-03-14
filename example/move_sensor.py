from machine import Pin
import utime

pir_sensor = Pin(28,Pin.IN)
led = Pin(15,Pin.OUT)

while True :
    if pir_sensor.value()==1:
        for i in range(2):
            led.toggle()
            utime.sleep(1)
        else:
            led.value(0)
    else:
        led.value(0)
        
            
