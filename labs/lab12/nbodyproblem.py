from nbodyhelpers import Vec2
from nbodyhelpers import Particle
import math
import random
SIZE_CONSTANT = 1/10
BIG_G = 2000
TIME_STEP = 0.1
def gravity(bodyA: Particle, bodyB: Particle) -> Vec2:
    distance_x = bodyA.pos.x - bodyB.pos.x
    distance_y = bodyA.pos.y - bodyB.pos.y
    distance = Vec2(distance_x, distance_y).magnitude()
    direction = math.atan2(distance_y, distance_x)
    magnitude = (BIG_G * bodyA.mass * bodyB.mass) / (distance ** 2)
    force = Vec2(magnitude * math.cos(direction), magnitude * math.sin(direction))
    return force

class Body(Particle):
    def __init__(self, mass: float, pos: Vec2, vel: Vec2) -> None:
        Particle.__init__(self, mass, pos, vel)
        self.t.shapesize(SIZE_CONSTANT*self.mass**(1/3))
    def apply_force(self: Vec2, force: Vec2) -> None:
        ax = force.x / self.mass
        ay = force.y / self.mass
        self.accelerate(Vec2(ax, ay), TIME_STEP)
        
def simulate(bodies: list[Body]) -> None:
    forces = []
    for i in range(0, len(bodies)):
        forces.append(Vec2(0, 0))
    for i in range(0, len(bodies) - 1):
        for j in range(i + 1, len(bodies)):
            gravitation_force = gravity(bodies[i], bodies[j])
            forces[i] = forces[i] - gravitation_force
            forces[j] = forces[j] + gravitation_force
    for i in range(0, len(bodies)):
        bodies[i].apply_force(forces[i])

def main():
    bodies =  []
    for i in range(0, 12):
        init_pos = Vec2(random.uniform(-200, 200), random.uniform(-200, 200))
        init_vel = Vec2(random.uniform(-20, 20), random.uniform(-20, 20))
        new_body = Body(random.uniform(10, 60), init_pos, init_vel)
        bodies.append(new_body)
    # bodies.append(Body(30, Vec2(200, 0), Vec2(0, 150)))
    # bodies.append(Body(4000, Vec2(0, 0), Vec2(0, 0)))
    while True:
        simulate(bodies)


if __name__ == "__main__":
    main()