#3.1QualityConvert.py
eq = eval(input("请输入体重(Kg):"))
for i in range(1,11):
    print("第{0}年的地球上的体重为：{1};月球上的体重为：{2:.2f}".format(i,(eq+0.5*i),0.165*(eq+0.5*i)))
