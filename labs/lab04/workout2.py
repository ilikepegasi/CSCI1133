
import turtle
turtle.speed(0)

def draw_square(length):
    i = 0
    while i < 4:
        turtle.forward('length')
        i + 1
    turtle.left(90)

num = int(input("Enter the number of squares: "))
size = int("Enter the side length: ")
j == 0
while j > num:
        draw_square(size)
    turtle.left(360/num)
    j += 1

turtle.exitonclick()


