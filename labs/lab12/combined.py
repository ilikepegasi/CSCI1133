import turtle
turtle.screensize(1000, 1000)


class Vec2():
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    def get_values(self) -> list:
        return [self.x, self.y]
    def set_values(self, new_values: list) -> None:
        self.x = new_values[0]
        self.y = new_values[1]
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2)**(1/2)
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, num:str):
        return Vec2(self.x * num, self.y * num)

class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass #this is a float or int
        self.pos = pos #this is a Vec2 object
        self.vel = vel #this is a Vec2 object
        self.t = turtle.Turtle()	#don’t forget to import turtle!
        self.t.shape("circle")
        self.t.speed(0)
        self.t.penup()
        self.move()  #uncomment this after you implement move()
        self.t.pendown()
    def __str__(self) -> str:
        return f"mass:{self.mass}, pos:{str(self.pos)}, vel:{str(self.vel)}"
    def move(self) -> None:
        self.t.setpos(min(self.pos.x, 1000), min(self.pos.y, 1000))
    def accelerate(self, a:Vec2, t:float) -> None:
        self.pos.x = self.pos.x + self.vel.x * t + 0.5 * a.x * t**2
        self.pos.y = self.pos.y + self.vel.y * t + 0.5 * a.y * t**2
        self.vel.x = self.vel.x + a.x * t
        self.vel.y = self.vel.y + a.y * t
        self.move()



if __name__ == '__main__':
    mass = 0.5
    accel1 = Vec2(1, 2)
    print(accel1) #should output <1, 2>
    accel2 = Vec2(2, -2)
    total_accel = accel1 + accel2
    print(total_accel) #should output <3, 0>
    force = total_accel * mass
    flist = force.get_values()
    print(flist) #should output [1.5, 0.0]
    accel1.set_values(flist)
    print(accel1) #should output <1.5, 0.0>


if __name__ == '__main__':
    p1 = Particle(50,Vec2(-200,-50),Vec2(30,30))
    p2 = Particle(20,Vec2(100,50),Vec2(-20,0))
    print(p2) #should output mass:20, pos:<100, 50>, vel:<-20, 0>
    p2.accelerate(Vec2(0,-10),2)
    print(p2) #should output mass:20, pos:<60.0, 30.0>, vel:<-20, -20>
    p2.accelerate(Vec2(20,20),3)
    print(p2) #should output mass:20, pos:<90.0, 60.0>, vel:<40, 40>
    for i in range(100):
        p1.accelerate(Vec2(0,-10),0.1)
        p2.accelerate(Vec2(0,-10),0.1)
    print(p1) #should output mass:50, pos:<100.0, -250.0>, vel:<30.0, -70.0>
    print(p2) #should output mass:20, pos:<490.0, -40.0>, vel:<40.0, -60.0>
    turtle.exitonclick()
