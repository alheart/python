#!/bin/python

def move(n, a, b, c):
    if (n == 1):
        print("%s --> %s" % (a, c))
    else:
        move(n-1, a, c, b)
        print("%s --> %s" % (a, c))
        move(n-1, b, a, c)


def pas_triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
