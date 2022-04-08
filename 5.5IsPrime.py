#5.5IsPrime.py
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True
try:
    num = int(input("请输入一个整数："))
    print(isPrime(num))
except:
    print("输入格式错误")

    
