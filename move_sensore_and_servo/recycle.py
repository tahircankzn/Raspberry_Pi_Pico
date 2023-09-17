from machine import Pin, PWM
import utime
import time

servo = PWM(Pin(15))

servo.freq(50)


trig = Pin(2,Pin.OUT)
echo = Pin(3,Pin.IN)

red = Pin(13,Pin.OUT)
green = Pin(9,Pin.OUT)             
    
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
    return high - low

while True:
    red.value(1)
    if distance() < 500:
        red.value(0)
        green.value(1)
        counter = 0
        x = 1350
        for y in range(1350,8200):
            if x > 8200:
                counter +=1
                x = 1350
            else:
                x+=10
                servo.duty_u16(x)
            #print(x)
            utime.sleep(0.01)
            if counter == 1:
                x = 8200
                for y in range(1350,8200):
                    if x < 1350:
                        
                        x = 1350
                        break
                    else:
                        x-=10
                        servo.duty_u16(x)
                    #print(x)
                    utime.sleep(0.01)
                
                green.value(0)
                
                break

    

