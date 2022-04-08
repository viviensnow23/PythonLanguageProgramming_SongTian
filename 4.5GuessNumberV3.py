#4.5GuessNumberV3.py
import random
num = random.randint(0,100)
N = 0
while 1:
    N += 1
    try:
        guess = eval(input("请输入数字："))
    except NameError:
        print("输入内容必须为整数！")
    else:
        if guess > num:
            print("遗憾，太大了")
        elif guess < num:
            print("遗憾，太小了")
        else:
            print("预测{}次，你猜中了！".format(N))
            break

