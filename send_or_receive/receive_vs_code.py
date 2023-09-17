import serial # Serial modülünü içe aktar
import time # Time modülünü içe aktar

ser = serial.Serial('COM4', 9600) # Seri port nesnesi oluştur. COM portunu ve baud hızını değiştirebilirsiniz.
time.sleep(2) # Seri portun açılması için 2 saniye bekle

while True: # Sonsuz döngü başlat
    #data = ser.readline().decode('utf-8') # Seri porttan gelen veriyi oku ve utf-8 formatına çevir
    #print(data) # Veriyi ekrana yazdır
    key = input("Veri göndermek için s, çıkmak için q tuşuna basın: ") # Kullanıcıdan girdi al
    if key == "s": # Eğer girdi s ise
        message = input("Göndermek istediğiniz mesajı yazın: ") # Kullanıcıdan mesaj al
        ser.write(message.encode('utf-8')) # Mesajı utf-8 formatına çevirip seri porttan gönder
    elif key == "q": # Eğer girdi q ise
        break # Döngüden çık

ser.close() # Seri portu kapat
