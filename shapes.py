import turtle
import math

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)

# Square
myPen.up()
myPen.setposition(-100, -100)
myPen.down()
myPen.fd(200)
myPen.left(200)
myPen.fd(200)
myPen.left(90)
myPen.fd(200)
myPen.left(90)
myPen.fd(200)
myPen.left(90)

# Cirlce
myPen.up()
myPen.setposition(0, -100)
myPen.down()
myPen.circle(100)
