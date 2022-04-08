#5.4Multi.py
def multi(a,*b):
    for n in b:
        a *= n
    return a
print(multi(1,2,3,4,5))
