#3.4PalindromicNumber.py
num = input("请输入一个5位数字：")
numPa = num[::-1]
if len(num) == 5:
    try:
        if int(num) == int(numPa):
            print(num,"是回文数")
        else:
            print(num,"不是回文数")
    except Exception as e:
        print(e)
        print(num,"含有其他字符")
else:
    print(num,"不是5位数")
123
