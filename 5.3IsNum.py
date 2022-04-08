#5.3IsNum.py
def isNum(str1):
    try:
        words = type(eval(str1))
        if words == type(1):
            return "True"
        elif words == type(1.0):
            return "True"
        elif words == type(1 + 1j):
            return "True"
    except:
        return "False"
str1 = input("请输入：")
print(isNum(str1))

    
