#5.6Datetime&Birthday.py
from datetime import datetime
birthday = datetime(1996,11,23,00,00,00)
print(birthday)
print(birthday.weekday())
print(birthday.strftime("%Y-%m-%d %H:%M:%S"))
print(birthday.strftime("%Y %m %d %H:%M:%S"))
birthday.strftime("%Y %m %d %H:%M:%S")
print("{0:%Y}年{0:%m}月{0:%d}日".format(birthday))
print(birthday.strftime("%Y-%B-%d"))
print(birthday.strftime("%Y-%b-%d"))
print(birthday.strftime("%Y-%B-%d %A"))
print(birthday.strftime("%Y-%b-%d %a"))
