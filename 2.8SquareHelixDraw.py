#2.8SquareHelixDraw.py
import turtle
import random
turtle.setup(700,700)
turtle.pensize(1)
turtle.pencolor("black")
turtle.seth(0)
for i in range(200):
    turtle.fd(2*i)
#    a = random.uniform(0,1)
#    b = random.uniform(0,1)
#    c = random.uniform(0,1)
#    turtle.pencolor(a,b,c)
    turtle.left(90)
turtle.done()
