#!/bin/python

def MyAbs(x):
    if x >= 0:
        return x
    else:
        return -x

print("abs [-5] is %s %s" % (MyAbs(-5), -5))
