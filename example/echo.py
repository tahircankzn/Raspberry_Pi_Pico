from machine import Pin
import utime

trigger = Pin(18,Pin.OUT)
echo = Pin(21,Pin.IN)


def echoTime():
    trigger.value(0)
    utime.sleep_us(5)
    trigger.value(1)
    utime.sleep_us(10)
    trigger.value(0)
    try:
        echoTime = machine.time_pulse_us(echo , 1 , 1000000)
        cm = (echoTime * 0.0334321)
        
        if cm <= 20:
            print(str(cm) + "cm")
    except OSError as e:
        print(e)
        
        
while True:
    echoTime()
    utime.sleep(5)
