from machine import Pin, Timer
import time

led = Pin(25,Pin.OUT) # 25. pin kart üzerinde bulunan led ışığa ait
#          |
#          v
#      Pin Numarası   : GP25

while True :
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)


# Harici bir led için yapmamız gereken tek şey GP10(Pin Numarası 10) vb şeklinde pine led bağlamak
# Görseli inceleyiniz
