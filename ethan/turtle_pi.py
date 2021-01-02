import random
import turtle
import math
import matplotlib.pyplot as plt

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
r = 100 # radius of circle (and half side length of square because circle inscribed)

# Square with side length 2*r
myPen.up()
myPen.setposition(-r,-r)
myPen.down()
myPen.fd(2*r)
myPen.left(90)
myPen.fd(2*r)
myPen.left(90)
myPen.fd(2*r)
myPen.left(90)
myPen.fd(2*r)
myPen.left(90)

# Cirlce with radius, r
myPen.up()
myPen.setposition(0,-r)
myPen.down()
myPen.circle(r)

def monteCarlo(n):
    in_circle = 0
    out_circle = 0
    pi_values,error = [],[]
    for i in range(n):
        # generating random coordinate point inside square
        x = random.randrange(-100,100)
        y = random.randrange(-100,100)

        # if less than radius away from center --> is in circle --> plot black point
        if(x**2+y**2>100**2):
            myPen.color("black")
            myPen.up()
            myPen.goto(x,y)
            myPen.down()
            myPen.dot()
            out_circle += 1
        
        # else plot red point
        else:
            myPen.color("red")
            myPen.up()
            myPen.goto(x,y)
            myPen.down()
            myPen.dot()
            in_circle += 1

        # deriving value of pi from area estimates
        square_area_estimate = in_circle+out_circle
        circle_area_estimate = in_circle
        pi = 4.0 * circle_area_estimate / square_area_estimate
        pi_values.append(pi)

        # calculating difference between estimate and actual value
        error.append(math.pi - pi)

    return [pi_values,error]

results = monteCarlo(1000)

#plotting results
plt.figure(dpi=200)
plt.axhline(y=math.pi,color='red',linestyle='dashed')
plt.plot(results[0])
plt.xlabel('Iterations')
plt.ylabel('Pi')
plt.savefig('pi_estimate.png')

#plotting error
plt.figure(dpi=200)
plt.axhline(y=0,color='red',linestyle='dashed')
plt.plot(results[1])
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.savefig('pi_error.png')