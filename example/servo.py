from machine import Pin, PWM
import utime

servo = PWM(Pin(15))

servo.freq(50)






def engine():
    while True:
        servo.duty_u16(1350)
        utime.sleep(1)
        servo.duty_u16(8200)
        utime.sleep(1)


def engine1():
    size = 1350

    while size <=8200:
        servo.duty_u16(size)
        size+=500
        utime.sleep(0.5)
        
def engine2():
    x = 1320
    
    while True:
        for y in range(1350,8200):
            if x > 8200:
                
                x = 1350
            else:
                x+=10
                servo.duty_u16(x)
            utime.sleep(0.01)
engine2()               
    


    