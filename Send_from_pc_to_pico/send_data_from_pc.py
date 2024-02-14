import serial
import time

s = serial.Serial(port="COM12", parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
s.flush()

def main():
    

    s.write("123\r".encode())
    mes = s.read_until().strip()
    print(mes.decode())


if __name__ == "__main__":
    while 1:
        main()
        time.sleep(1)