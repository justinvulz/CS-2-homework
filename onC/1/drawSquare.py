def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

import turtle
import time

turtle.speed(2)

alex = turtle.Turtle()



drawSquare(alex, 50)

