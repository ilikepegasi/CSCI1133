import turtle
import random
def main():
    turtle.speed(0)
    for i in range(0, 200):
        turtle.forward(30)
        turtle.setheading(random.randint(0, 3) * 90)
    turtle.exitonclick()

main()