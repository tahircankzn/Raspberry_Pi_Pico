from machine import Pin
import time

#led_green = Pin(15,Pin.OUT)
button = Pin(17,Pin.IN,Pin.PULL_DOWN) # PULL_DOWN veri gitmiyorken 
# hep 0 sinyali (0 sinyali butona basılmadı demek) gönderir böylece sinyal karışıklığı engellenir
# PULL_UP ise 1 sinyali gönderir ve butona basılmış gibi sinyal gönerir

# button olmadan da button kullanabiliriz , 2 kaplonun birini 17. pine diğerini 3v3(out) a bağlarız
# 2 kaployu temas ettirirsek buttona basılmış olur , ayırırsak butona basılmamış olur

while True :
    print(button.value())
    time.sleep(0.5)