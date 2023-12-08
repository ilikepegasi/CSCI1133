import turtle, random

def random_position():
    new_x = 15 + 30*random.randint(0,19)
    new_y = 15 + 30*random.randint(0,19)
    position = (new_x, new_y)
    return position
    
class Game:
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        
        self.snake1 = Snake(315, 315, "green")
        self.foods = []
        for i in range(0, 20):
            self.foods.append(Food("red", foods, snake1))
        #These two lines must always be at the BOTTOM of __init__
        self.gameloop()
        turtle.onkeypress(self.snake1.go_down, 'Down')
        turtle.onkeypress(self.snake1.go_up, 'Up')
        turtle.onkeypress(self.snake1.go_left, 'Left')
        turtle.onkeypress(self.snake1.go_right, 'Right')
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        self.snake1.move(self.foods)
        if not self.snake1.collision():
            turtle.ontimer(self.gameloop, 200)
        else:
            turtle.penup()
            turtle.setpos(300, 300)
            turtle.write("bad girl", False, "left", ("Arial", 24, "normal"))

class Food():
    def __init__(self, color, foods, snake1):
        self.food = turtle.Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.shapesize(1.5, 1.5)
        self.food.color(color)
        self.x = x
        self.y = y
        self.food.move(foods, snake1)
    def move(self, foods, snake1):
        
        self.x = new_x
        self.y = new_y
        self.food.setpos(new_x, new_y)

class Snake():
    def __init__(self, x, y, color):
        self.segments = []
        self.x = x
        self.y = y
        self.color = color
        self.vx = 30
        self.vy = 0
        self.grow()
    def grow(self):
        seg = turtle.Turtle()
        seg.speed(0)
        seg.fillcolor(self.color)
        seg.shape("square")
        seg.shapesize(1.5, 1.5)
        seg.penup()
        seg.setpos(self.x, self.y)
        self.segments.append(seg)
    def move(self, foods):
        self.x += self.vx
        self.y += self.vy
        for food in foods:
            if self.x == food.x and self.y == food.y:
                food.move(foods, self)
                self.grow()
                return None
        for i, segment in enumerate(self.segments):
            if i == len(self.segments) - 1:
                segment.setpos(self.x, self.y)
            else:
                segment.setpos(self.segments[i + 1].pos())
    def collision(self):
        head_index = len(self.segments)-1
        head_pos = self.segments[head_index].pos()
        for i in range(0, head_index):
            if self.segments[i].pos() == head_pos:
                return True
        if head_pos[0] < 0 or head_pos[0] > 600 or head_pos[1] < 0 or head_pos[1] > 600:
            return True
        return False
        

    def go_down(self):
        if self.vy != 30:
            self.vy = -30
            self.vx = 0
    def go_up(self):
        if self.vy != -30:
            self.vy = 30
            self.vx = 0
    def go_right(self):
        if self.vx != -30:
            self.vx = 30
            self.vy = 0
    def go_left(self):
        if self.vx != 30:
            self.vx = -30
            self.vy = 0
    
if __name__ == '__main__':
    Game()
