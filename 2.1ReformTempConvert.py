#2.1ReformTempConvert.py
TempNum = eval(input("请输入温度(无单位)："))
TempUnit = input("请输入温度单位：")
if TempUnit in ['f','F']:
    C = (TempNum - 32)/1.8
    print("转换后的温度是：{:.0f}".format(C))
elif TempUnit in ['c','C']:
    F = 1.8*TempNum + 32
    print("转换后的温度是：{:.0f}".format(F))
else:
    print("输入格式错误")
