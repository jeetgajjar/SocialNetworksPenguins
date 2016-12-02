import random

def comp(r,g,b):
    x = ((r / 4) * (64 ** 2)) + ((g / 4) * (64)) + ((b / 4))
    return x


def deco(x):
    b = (x % 64) * 4
    g = ((x / 64) % 64) * 4
    r = ((x / (64 ** 2))) * 4
    return r,g,b

def edge_comp(a,b):
    return long(a) * 262144 + long(b)

def edge_deco(x):
    b = int(x % 262144)
    a = int(x / 262144)
    return a,b

for i in range(1):
    a = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    b = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

    x = edge_comp(comp(a[0],a[1],a[2]),comp(b[0],b[1],b[2]))

    ap,bp = edge_deco(x)

    print str(a) + " " + str(deco(ap))
    print str(b) + " " + str(deco(bp))
    print
