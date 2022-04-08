#5.7Hanoi.py
count = 0
def hanoi(n,src,dst,mid):#n为盘子数量，a为起始柱，b为中间柱，c为结束柱子
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)
hanoi(3,"A","B","C")
print(count)
