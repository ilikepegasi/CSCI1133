from combined import Vec2
from combined import Particle
import math
import random
BIG_G = 10
TIME_STEP = 0.1
def gravity(bodyA:Particle, bodyB:Particle) -> Vec2:
    distance_x = bodyA.pos.x - bodyB.pos.x
    distance_y = bodyA.pos.y - bodyB.pos.y
    try:
        force_magnitude_x = (BIG_G * bodyA.mass * bodyB.mass) / (distance_x**2)
    except ZeroDivisionError:
        force_magnitude_x = 1
    try:
        force_magnitude_y = (BIG_G * bodyA.mass * bodyB.mass) / (distance_y**2)
    except ZeroDivisionError:
        force_magnitude_y = 1
    force_vector = Vec2(force_magnitude_x, force_magnitude_y)
    return force_vector

def simulate(bodies:list) -> None:
    for body in bodies:
        body.force.set_values([0, 0])
    for i in range(0, len(bodies)-1):
        for j in range(i+1, len(bodies)):
            calculated_force = gravity(bodies[i], bodies[j])
            print(calculated_force)
            bodies[i].force += calculated_force
            bodies[j].force -= calculated_force
    for body in bodies:
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
    for i in range(0, 6):
        init_pos = Vec2(random.uniform(-200, 200), random.uniform(-200, 200))
        init_vel = Vec2(random.uniform(-25, 25), random.uniform(-25, 25))
        new_body = Body(random.uniform(3, 6), init_pos, init_vel, Vec2(0, 0))
        bodies.append(new_body)
    bodies.append(Body(1000, Vec2(0, 0), Vec2(0, 0), Vec2(0, 0)))
    while True:
        simulate(bodies)


if __name__ == "__main__":
    main()