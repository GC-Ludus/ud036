import turtle

def drawSquare(myTurtle):
    for x in range(1, 5):
        myTurtle.forward(100)
        myTurtle.right(90)
    
def drawCircle():
    ibba = turtle.Turtle()
    ibba.circle(50)
    
def drawTriangle():
    ibba = turtle.Turtle()
    steps = 3
    for x in range(0, steps):
        ibba.forward(100)
        ibba.right(120)

def drawArt():
    window = turtle.Screen()
    window.bgcolor('red')

    ibba = turtle.Turtle()
    ibba.shape('turtle')
    ibba.color('yellow')
    ibba.speed(10)
    
    density = 10
    count = 360 / density
    for i in range(1, count):
        drawSquare(ibba)
        ibba.right(density)
    
    # drawCircle()
    # drawTriangle()
    window.exitonclick()

drawArt()
