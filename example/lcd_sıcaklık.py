import utime
from machine import I2C, Pin , ADC , Timer
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

led = Pin(25,Pin.OUT)
sensor_temp = ADC(4) # 4 numaralı pinde sıcaklık sensörü var
conversion_factor = 3.3 / (65535)
timer = Timer() #####


def blink(timer): #####
    led.toggle()


def Sıcaklık():
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706)/0.001721
        temperature1 = str(temperature)[0:5]
        if temperature < 25:
            timer.init(freq=1,mode=Timer.PERIODIC,callback=blink)
            print("sıcaklık {}".format(temperature))
            temperature = str(temperature)[0:5]
            
                           
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Tahir Can Kozan")
            lcd.move_to(0,1)
            lcd.putstr("sıcaklık {}".format((temperature1)))
            sleep(2)
            
            

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def greeting():
    
    lcd.clear()
    sleep(2)
    lcd.move_to(3,0)
    lcd.putstr("Termometre")
    lcd.move_to(6,1)
    lcd.putstr("")
    utime.sleep(2)
    lcd.clear()

    


def customcharacter():
    
  #character      
  lcd.custom_char(0, bytearray([
  0x0E,
  0x0E,
  0x04,
  0x1F,
  0x04,
  0x0E,
  0x0A,
  0x0A
        
        ]))
  
    #character2      
  lcd.custom_char(1, bytearray([
    0x1F,
  0x15,
  0x1F,
  0x1F,
  0x1F,
  0x0A,
  0x0A,
  0x1B
        
        ]))
  
  
  
  
  #smiley
  lcd.custom_char(2, bytearray([
  0x00,
  0x00,
  0x0A,
  0x00,
  0x15,
  0x11,
  0x0E,
  0x00
        
        ]))
  
  #heart
  lcd.custom_char(3, bytearray([
   0x00,
  0x00,
  0x0A,
  0x15,
  0x11,
  0x0A,
  0x04,
  0x00
        
        ]))
  
      #note
  lcd.custom_char(4, bytearray([
   0x01,
  0x03,
  0x05,
  0x09,
  0x09,
  0x0B,
  0x1B,
  0x18
        
        ]))
    #celcius
  lcd.custom_char(5, bytearray([
  0x07,
  0x05,
  0x07,
  0x00,
  0x00,
  0x00,
  0x00,
  0x00
        
        ]))
  

    

    
greeting()    
customcharacter()

Sıcaklık()



#
#lcd.move_to(0,1)
#lcd.putchar(chr(0))
#lcd.move_to(4,1)
#lcd.putchar(chr(1))
#cd.move_to(8,1)
#lcd.putchar(chr(2))
#lcd.move_to(12,1)
#lcd.putchar(chr(3))
#lcd.move_to(15,1)
#lcd.putchar(chr(4))