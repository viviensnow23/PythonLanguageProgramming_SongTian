#2.6CornerlessSquare.py
import turtle
turtle.setup(650,650)
turtle.penup()
turtle.fd(-200)
turtle.seth(-90)
turtle.fd(200)
turtle.seth(0)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor("black")
def drawGap():
    turtle.penup()
    turtle.fd(20)
    turtle.pendown()
def drawLine():
    drawGap()
    turtle.fd(360)
    drawGap()
    turtle.left(90)
for i in range(4):
    drawLine()
turtle.done()
    

