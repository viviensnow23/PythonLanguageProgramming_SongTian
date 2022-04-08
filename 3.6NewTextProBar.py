#3.6NewTextProBar.py
import time
scale = 10
print("Starting",end ="")
for i in range(scale+1):
    a = '·'*i
    b = ' '*(scale-i)
    print('/r',a,b,end = "")
    time.sleep(0.3)
print("Done")
    
