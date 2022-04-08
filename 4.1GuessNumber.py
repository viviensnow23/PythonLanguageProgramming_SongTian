#4.1GuessNumberV1.py
num = 5
N = 1
guess = eval(input("请输入数字："))
while num != guess:
    if guess > num:
        print("遗憾，太大了")
    else:
        print("遗憾，太小了")
    guess = eval(input("请输入数字："))
    N += 1
else:
    print("预测{}次，你猜中了！".format(N))

