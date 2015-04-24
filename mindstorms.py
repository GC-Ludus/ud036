import turtle

def drawSquare():
    ibba = turtle.Turtle()
    ibba.shape('circle')
    ibba.color('green')
    ibba.speed(2.5)
    
    steps = 4
    for x in range(0, steps):
        ibba.forward(100)
        ibba.right(90)
    
def drawCircle():
    ibba = turtle.Turtle()
    ibba.circle(50)
    
def drawTriangle():
    ibba = turtle.Turtle()
    steps = 3
    for x in range(0, steps):
        ibba.forward(100)
        ibba.right(120)
    
window = turtle.Screen()
window.bgcolor('red')
drawSquare()
drawCircle()
drawTriangle()
window.exitonclick()
