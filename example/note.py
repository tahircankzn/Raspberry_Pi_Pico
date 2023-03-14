from machine import Pin , ADC , Timer
from time import sleep
led = Pin(25,Pin.OUT)

timer = Timer() #####


def blink(timer): #####
    led.toggle()


def note():
    
    a = int(input("not 1 :"))
    b = int(input("not 2 :"))
    c = a+b
    
    if c > 60:
        led.toggle() # ledi açar
    
        print("geçti")
        sleep(1)
        led.value(0) # ledi kapatır
    else:
        print("kaldı")
         
note()



    
    
# main.py olarak kaydedersek pico harici güç adaptörüne bağlıykende kod çalışr 
