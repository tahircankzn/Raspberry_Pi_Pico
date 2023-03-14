from machine import Pin
import time

led_green = Pin(15,Pin.OUT)
button = Pin(14,Pin.IN,Pin.PULL_DOWN) # PULL_DOWN veri gitmiyorken 
# hep 0 sinyali (0 sinyali butona basılmadı demek) gönderir böylece sinyal karışıklığı engellenir
# PULL_UP ise 1 sinyali gönderir ve butona basılmış gibi sinyal gönerir

while True :
    if button.value():
        led_green.toggle()
        print("butona basıldı",button.value())
    time.sleep(0.5)