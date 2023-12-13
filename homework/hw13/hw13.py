import turtle, random

def grid():
    all_positions = []
    for x in range(15, 15+19*31, 30):
        for y in range(15, 15+19*31, 30):
            all_positions.append((x, y))
    return all_positions

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
        turtle.tracer(0, 0)
        turtle.speed(0)
        self.delay = 200
        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        self.positions = grid()
        self.snake1 = Snake(315, 315, "green")
        self.foods = []
        for i in range(0, 1):
            self.foods.append(Food("red", self.foods, self.snake1))
        self.gameloop()
        turtle.onkeypress(self.snake1.go_down, 'Down')
        turtle.onkeypress(self.snake1.go_up, 'Up')
        turtle.onkeypress(self.snake1.go_left, 'Left')
        turtle.onkeypress(self.snake1.go_right, 'Right')
        turtle.onkeypress(self.slow, '1')
        turtle.onkeypress(self.medium, '2')
        turtle.onkeypress(self.fast, '3')
        turtle.listen()
        turtle.mainloop()
    def slow(self):
        self.delay = 300
    def medium(self):
        self.delay = 200
    def fast(self):
        self.delay = 133
    def gameloop(self):
        self.snake1.move(self.foods)
        if not self.snake1.collision():
            turtle.ontimer(self.gameloop, self.delay)
        else:
            turtle.penup()
            turtle.setpos(215, 300)
            turtle.write("Game OVER", False, "left", ("Arial", 48, "normal"))
        turtle.update()

class Food():
    def __init__(self, color, foods, snake1):
        self.food = turtle.Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.shapesize(1.5, 1.5)
        self.food.color(color)
        self.move(foods, snake1)
    def move(self, foods, snake1):
        illegal_positions = []
        positions = grid()
        for food in foods:
            illegal_positions.append((food.x, food.y))
        for segment in snake1.segments:
            illegal_positions.append(segment.pos())
        for illegal_position in illegal_positions:
            positions.remove(illegal_position)
        try:
            new_pos = random.choice(positions)
        except:
            turtle.write("good girl ;)", False, "left", ("Arial", 48, "normal"))
        self.x = new_pos[0]
        self.y = new_pos[1]
        
        self.food.setpos(self.x, self.y)

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
