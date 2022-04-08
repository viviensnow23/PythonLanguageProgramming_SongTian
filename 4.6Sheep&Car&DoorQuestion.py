#4.6Sheep&Car&DoorQuestion.py
import random 
d1 = 'sheep'
d2 = 'sheep'
d3 = 'car'
C1 = 0
N1 = 0
C2 = 0
N2 = 0
while N1 < 1000:
    N1 += 1
    choice = random.randint(1,3)
    if choice == 3:
        C1 += 1
else:
    print("不改变选择获胜的机率是：{}".format(C1/N1))
while N2 < 1000:
    N2 += 1
    choice = random.randint(1,3)
    if choice == 1:
        C2 += 1
    elif choice == 2:
        C2 += 1
    else:
        C2 += 0
else:
    print("改变选择获胜的机率是：{}".format(C2/N2))

