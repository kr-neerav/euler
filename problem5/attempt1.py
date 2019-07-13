#!/usr/bin/env python


def is_small(a:int, b:int) -> bool:
    """check if a is smaller than or equal to b"""
    return a <= b

def get_remainder(n:int, d:int) -> int:
    """return the remainder when n is divided by d"""
    return n%d

def hcf(a:int, b:int) -> int:
    """find the hcf of a and b"""
    if b == 0:
        return a
    return hcf(b, get_remainder(a,b))

def lcm(a:int, b:int) -> int:
    """find the lcm of a and b"""
    return int(a*b/hcf(a,b))

num_list = range(3,21)

a = 2
for b in num_list:
    a = lcm(a,b)

print(a)
