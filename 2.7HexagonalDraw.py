#2.7HexagonalDraw.py
import turtle
turtle.setup(650,650)
turtle.penup()
turtle.fd(-100)
turtle.seth(90)
turtle.fd(50)
turtle.pendown()
def drawHexagon():
    turtle.fd(100)
    turtle.right(60)
def drawAngle():
    turtle.fd(100)
    turtle.right(120)
    turtle.fd(100)
    turtle.left(60)
turtle.seth(30)
for i in range(6):
    drawHexagon()
turtle.seth(90)
for i in range(6):
    drawAngle()
turtle.done()
