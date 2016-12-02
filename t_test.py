import random

def comp(r,g,b):
    #x = ((r * 16 * 64)) + (g * 16) + (b / 4)
    x = ((r / 4) * (64 ** 2)) + ((g / 4) * (64)) + ((b / 4))
    return x


def deco(x):
    b = (x % 64) * 4
    g = ((x / 64) % 64) * 4
    r = ((x / (64 ** 2))) * 4
    return r,g,b

for i in range(100):
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rp, gp, bp = deco(comp(r,g,b))
    print str((r,g,b)) + " " + str((rp,gp,bp)) + "\t\t" + str(max(abs(r - rp),abs(g - gp), abs(b - bp)))
