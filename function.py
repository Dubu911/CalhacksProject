
import random


def gravity(x):
    if x == 0:
        y = 1
    y = x * 1.1

    if 640 > y > 630:
        y = 630
        z = random.randrange(1, 4)
        if z > 1:
            y = 0
            return y
    if y > 640:
        y = 0
    return y


z = random.randrange(1, 4)
print(z)