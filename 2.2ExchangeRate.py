#2.2ExchangeRate.py
# 1 RMB = 1/6 dollar，1 Dollar = 6 RMB
intro = "输入美元或人民币的金额，美元以D结尾，人民币以R结尾"
print(intro)
m = input("请输入金额：")
if m[-1] == 'D':
    RMB = 6*float(m[0:-1])
    print("{}美元为{:.2f}人民币".format(m[0:-1],RMB))
elif m[-1] == 'R':
    Dollar = 1/6*float(m[0:-1])
    print("{}人民币为{:.2f}美元".format(m[0:-1],Dollar))
else:
    print("输入格式错误")
