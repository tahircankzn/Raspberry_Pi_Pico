import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd




I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def greeting():
    
    lcd.clear()
    lcd.move_to(4,0)
    lcd.putstr("Welcome")
    lcd.move_to(2,1)
    lcd.putstr("To My Github")
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
lcd.move_to(5,0)
lcd.putstr("Hello")
lcd.move_to(5,1)
lcd.putstr("World")

