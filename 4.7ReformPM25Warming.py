#4.7ReformPM25Warming.py
try:
    PM = eval(input("请输入PM2.5数值："))
    if 0 <= PM <= 35:
        print("空气优质，快去户外运动！")
    elif 35 <= PM < 75:
        print("空气良好，适度户外运动！")
    else:
        print("空气污染，请小心！")
except:
    print("数据类型错误")
