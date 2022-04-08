#Recursion.py
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]+s[0])

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

count = 0
def hanoi(n,src,dsc,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count = count + 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count = count + 1
        hanoi(n-1,mid,dst,src)
