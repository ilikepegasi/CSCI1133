
import turtle
turtle.speed(0) #Change this to 0 to speed up the turtle

def triangle(side):
    turtle.forward(side) #Move forward
    turtle.left(120) #Turn 120 degrees
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)



def triforce(side):
    
    triangle(side/2)
    turtle.forward(side) 
    turtle.left(120)
    triangle(side/2)
    turtle.forward(side)
    turtle.left(120)
    triangle(side/2)
    turtle.forward(side)
    turtle.left(120)

def triception(side):
    length = side * 0.5
    triforce(length)
    turtle.forward(side) 
    turtle.left(120)
    triforce(length)
    turtle.forward(side)
    turtle.left(120)
    triforce(length)
    turtle.forward(side)
    turtle.left(120)
triception(90)
turtle.exitonclick()