#4.2CountChr.py
a = input("请输入字符：")
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alpN = 0
num = "1234567890"
numN = 0
blank = " "
blankN = 0
othN = 0
for i in a:
    if i in alp:
        alpN += 1
    elif i in num:
        numN += 1
    elif i == " ":
        blankN += 1
    else:
        othN += 1
print("英文字符的个数是:{};数字的个数是:{};空格的个数是:{};其他字符的个数是:{}。".format(alpN,numN,blankN,othN))
