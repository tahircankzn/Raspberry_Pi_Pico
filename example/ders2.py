from machine import Pin , ADC , Timer
from time import sleep
import random
led = Pin(25,Pin.OUT)

timer = Timer() #####
"""
led.toggle() # ledi açar
    
        print("geçti")
        sleep(1)
        led.value(0) # ledi kapatır
"""
def note():
    liste = [1,2,3,4,5,6,7,8,9,10]
    cols = random.choice(liste)
    space = cols - 1
    star = 1  
    a = 1
    while a <= cols:
        print(space * " " + star * "*" + (star-1) * "*")
        print("\n")
        a+=1
        star+=1
        space-=1      
def hesap():
    liste = [1,2,3,4,5,6,7,8,9,10]
    
    
    for i in range(10):
        sayi1 = random.choice(liste)
        sayi2 = random.choice(liste)
        print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))
        sleep(1)
def game():
    liste = [1,2,3,4,5,6,7,8,9,10]
    
    
    for i in range(5):
        sayi1 = random.choice(liste)
        print("{}.sayı {}".format(i+1,sayi1))
        
        sleep(1)
        
def game1():
    liste = [1,2,3,4,5,6,7,8,9,10]
    liste2 = []
    liste3 = []
    a = 0
    for i in range(4):
        sayi1 = random.choice(liste)   
        liste3.append(sayi1)
    
    
    for i in range(4):
        sayi1 = int(input("{}. sayi : ".format(i+1)))     
        liste2.append(sayi1)
    for i in liste2:
        for l in liste3:
            if i == l:
                a+=1
            
    print("bilinen sayı adedi :{} \nkazanılan para :{}".format(a,a*5))
    
    
game1()



    
    
# main.py olarak kaydedersek pico harici güç adaptörüne bağlıykende kod çalışr 

