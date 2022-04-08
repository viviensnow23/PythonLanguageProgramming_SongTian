#4.3CommonDivisorAndCommonMultiple.py
a = eval(input("请输入一个数字："))
b = eval(input("请输入一个数字："))
if a>b:
    while a%b != 0:
        c = a%b
        a = b
        b = c
    print("最大公约数是：{}".format(c))
    print("最小公倍数是：{:.0f}".format(a*b/c))
elif a == b:
    print("最大公约数是：{}".format(a))
    print("最小公倍数是：{}".format(a))
else:
    while b%a != 0:
        c = b%a
        b = a
        a = c
    print("最大公约数是：{}".format(c))
    print("最小公倍数是：{:.0f}".format(a*b/c))
