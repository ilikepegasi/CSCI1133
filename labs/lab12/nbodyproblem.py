from combined import Vec2
from combined import Particle
import math
import random
BIG_G = 100
TIME_STEP = 0.001
def gravity(bodyA:Particle, bodyB:Particle) -> Vec2:
    distance_x = bodyA.pos.x - bodyB.pos.x
    distance_y = bodyA.pos.y - bodyB.pos.y
    distance = (distance_x**2 + distance_y**2)**0.5
    try:
        force_magnitude = (BIG_G * bodyA.mass * bodyB.mass) / (distance**2)
    except ZeroDivisionError:
        force_magnitude = 0
    force_direction = math.atan(distance_y / distance_x)
    force_vector = Vec2(force_magnitude*math.cos(force_direction), force_magnitude*math.sin(force_direction))
    return force_vector

def simulate(bodies:list) -> None:
    for i in range(0, len(bodies)-1):
        for j in range(i+1, len(bodies)):
            calculated_force = gravity(bodies[i], bodies[j])
            print(calculated_force)
            bodies[i].force += calculated_force
            bodies[j].force -= calculated_force
    for i, body in enumerate(bodies):
        body.apply_force()


class Body(Particle):
    def __init__(self, mass:float, pos:Vec2, vel:Vec2, force:Vec2) -> None:
        Particle.__init__(self, mass, pos, vel)
        self.force = force
    def apply_force(self) -> None:
        ax = self.force.x / self.mass
        ay = self.force.y / self.mass
        self.accelerate(Vec2(ax, ay), TIME_STEP)

def main():
    bodies =  []
    for i in range(0, 2):
        init_pos = Vec2(random.uniform(-200, 200), random.uniform(-200, 200))
        init_vel = Vec2(random.uniform(-50, 50), random.uniform(-50, 50))
        new_body = Body(random.uniform(3, 6), init_pos, init_vel, Vec2(0, 0))
        bodies.append(new_body)
    bodies.append(Body(1000, Vec2(0, 0), Vec2(0, 0), Vec2(0, 0)))
    while True:
        simulate(bodies)


if __name__ == "__main__":
    main()