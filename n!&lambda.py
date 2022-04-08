#def_n!&lambda.py
def fact1(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s
#fact(10)
#a = fact(10)
#print(a)

def fact2(n,m=1):
    s = 1
    for i in range(1,n+1):
        s = s*i
        return s//m
#fact(10)
#fact(10,5)

def fact3(n,*b):
    s = 1
    for i in range(1,n+1):
        s = s*i
    for item in b:
        s = s*item
    return s
#fact(10,3)
#fact(10,3,5,8)

def fact4(n,m=1):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s//m,n,m
#fact(10,5)
#a,b,c = fact(10,5)
#print(a,b,c)

n,s = 10,100
def fact5(n):
    s = 1
    for i in range(1,n+1):
        s = S*i
    return s
print(fact5(n),s)

n,s = 10,100
def fact6(n):
    global s
    for i in range(1,n+1)
    s = s*i
    return s
print(fact(n),s)

ls = ["F","f"]
def func(a):
    ls.append(a)
    return
func("c")
print(ls)

f = lambda x,y :x+y
#f(10,15)

f = lambda:"lambda函数“
#print(f())
