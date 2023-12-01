import turtle

def main():
    turtle.pensize(3)

    turtle.color("blue")
    turtle.circle(30)
    turtle.penup()
    turtle.goto(30, -30)
    turtle.pendown()
    turtle.color("yellow")
    turtle.circle(30)
    turtle.penup()
    turtle.goto(60, 0)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(30)
    turtle.penup()
    turtle.goto(90, -30)
    turtle.pendown()
    turtle.color("green")
    turtle.circle(30)
    turtle.penup()
    turtle.goto(120, 0)
    turtle.color("red")
    turtle.pendown()
    turtle.circle(30)

    turtle.exitonclick()

if __name__ == "__main__":
    main()