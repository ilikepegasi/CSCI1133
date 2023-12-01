import random as r
import turtle
def tree(t, trunk_length):
    if trunk_length > 15:
        trunk_length_s = r.randint(trunk_length-30, trunk_length)
        turtle.pencolor(1/trunk_length, 1, 1)
        turtle.pensize(trunk_length * 8)
        angle = r.randint(15, 45)
        t.forward(trunk_length_s)
        t.right(angle)
        tree(t, trunk_length-15)
        t.left(angle * 2)
        tree(t, trunk_length-15)
        t.right(angle)
        t.backward(trunk_length_s)

tree_turtle = turtle.Turtle()
tree_turtle.left(90)
tree_turtle.speed(0)
turtle.delay(0)
tree(tree_turtle,100)
turtle.exitonclick()
