
import turtle as t
import random

for i in range(100):
    r1 = random.randint(1, 10)
    steps = int(r1 * 100)
    angle = int(r1 * 20)
    t.right(angle)
    t.fd(steps)

t.mainloop()