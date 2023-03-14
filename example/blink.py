from machine import Pin, Timer

led_green = Pin(25,Pin.OUT)
timer = Timer()

def blink(timer):
    
    led_green.toggle()
    
timer.init(freq=1,mode=Timer.PERIODIC,callback=blink)