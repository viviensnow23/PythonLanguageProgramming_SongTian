#3.3NewDayDayUpV2.py
dayUp = 1
df = 0.01
for i in range(365):
    if i % 11 in [4,5,6,7]:
        dayUp *= 1 + df
    else:
        dayUp = dayUp
print("一年固定每10天休息一天的能力值是：{:.2f}".format(dayUp))
dayUp = 1
df = 0.01
for i in range(365):
    if i % 15 in [4,5,6,7,11,12,13,14]:
        dayUp *= 1 + df
    else:
        dayUp = dayUp
print("一年固定每15天休息一天的能力值是：{:.2f}".format(dayUp))

