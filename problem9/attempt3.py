#!/usr/bin/env python

def check_sum(a:int, b:int, c:int, limit:int) -> bool:
    """check if sum of a, b, c is less than limit"""
    return a + b + c == limit

def find_square(a:int) -> int:
    """find the square of a given a"""
    return a*a

found = False
limit = 1000
a = int(limit/3) - 1
b = int(limit/2) - 1
for i in range(1,a,1):
    for j in range(i+1,b,1):
        if (find_square(i) + find_square(j) == find_square(limit - i - j)):
            found = True
            break
    if found:
        break
print(i*j*(1000-i-j))
