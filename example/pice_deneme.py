import select
import utime
import sys

while True:
    
    if select.select([sys.stdin],[],[],0)[0]:
        ch = sys.stdin.read(2) 
        print(f"{ch}")
        if bb == "nice":
            print("nice")












