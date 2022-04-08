#3.2NewDayDayUpV1.py
dayUp = 1
df = 0.01
for i in range(365):
    if i%7 in [1,2,3]:
        dayUp = dayUp
    else:
        dayUp *= 1 + df
print("连续学习365天后能力值是：{:.2f}".format(dayUp))
