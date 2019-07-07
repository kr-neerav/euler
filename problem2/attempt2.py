#!/usr/bin/env python

def get_next(a:int, b:int) -> int:
    return a + b

upper_limit = 4000000
a = 1
b = 1
c = a + b
s = -2
while c <= upper_limit:
    s = s + c
    c = get_next(a,b)
    a = b + c
    b = a + c
print(s)
