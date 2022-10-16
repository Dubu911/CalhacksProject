
def gravity(x):
    if x == 0:
        y = 1
    y = x * 1.1
    if y >= 640:
        y = 640
    return y


