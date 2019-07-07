#!/usr/bin/env python

def get_next(a:int, b:int) -> int:
    return a + b

upper_limit = 4000000
a = 0
b = 1
c = a + b
s = 0
while c <= upper_limit:
    a = b
    b = c
    c = get_next(a,b)
    if c%2 == 0:
        s = s + c
print(s)
