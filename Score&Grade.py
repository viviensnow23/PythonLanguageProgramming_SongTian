#Score&Grades.py
score = eval(input())
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
print("输入成绩属于级别{}".format(grade))
    
