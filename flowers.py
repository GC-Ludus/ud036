import turtle
import math
    
def drawTriangle(myIbba):
    myIbba.forward(100)
    myIbba.right(150)
    myIbba.forward(100 * math.sin(math.radians(60)))
    myIbba.right(90)
    myIbba.forward(100 * math.cos(math.radians(60)))
    myIbba.right(120)

def drawArt():
    window = turtle.Screen()
    window.bgcolor('red')

    ibba = turtle.Turtle()
    ibba.shape('turtle')
    ibba.color('yellow')
    ibba.speed(10)
    
    density = 10
    count = 360 / density
    for i in range(0, count):
        drawTriangle(ibba)
        ibba.right(density)
    window.exitonclick()

drawArt()
