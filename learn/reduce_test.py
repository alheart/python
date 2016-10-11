#!/usr/bin/python3
# -*- coding: utf-8 -*-

def normalize(name):
    return name[0].upper() + name[1:].lower()

print(normalize("hello"))

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce
def prod(L):
    return reduce(lambda  x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def is_palindrome(n):
    nReserve=int(str(n)[::-1])
    return (nReserve == n)

output = filter(is_palindrome, range(1, 1000))
print(list(output))


def by_name(t):
    return t[0]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)


import functools

def log(text=""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('before %s:' % (func.__name__))
            if len(text) > 0:
                print('%s():' % (text))
            else:
                print('%s():' % (func.__name__))
            f=func(*args, **kw)
            print('after %s:' % (func.__name__))
            return f
        return wrapper
    return decorator

@log("execute")
def now():
    print('2015-3-25')

@log()
def now1():
    print('2015-3-26')

now()
now1()

