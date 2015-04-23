import turtle

def drawSquare():
    window = turtle.Screen()
    window.bgcolor('red')

    ibba = turtle.Turtle()
    ibba.shape('circle')
    ibba.color('green')
    ibba.speed(2.5)
    
    ibba.forward(200)
    steps = 3
    for x in range(0, steps):
        ibba.right(90)
        ibba.forward(200)
    
    window.exitonclick()

drawSquare()
