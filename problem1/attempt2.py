#!/usr/bin/env python

def is_divisible(i:int, j:int) -> bool:
    """return if i is divisible by j"""
    return i%j == 0

upper_limit = 1000
div1 = 3
div2 = 5
s = 0

for i in range(upper_limit):
    if  is_divisible(i, div1) or is_divisible(i, div2):
        s = s + i
print(s)
