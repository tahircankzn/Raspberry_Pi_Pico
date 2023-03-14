from machine import I2C , Pin
import utime

i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=4000000)

i2c_adres = i2c.scan()[0] # liste tip olduğu için 0. indeksten
# lcd ekranın adresini öğrenmemiz gerek

print(hex(i2c_adres)) # lcd ekran adresimizi ekrana yazdırdık
# lcd adresi 0x27



