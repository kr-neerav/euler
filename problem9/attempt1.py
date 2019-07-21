#!/usr/bin/env python

def check_sum(a:int, b:int, c:int, limit:int) -> bool:
    """check if sum of a, b, c is less than limit"""
    return a + b + c == limit

def find_square(a:int) -> int:
    """find the square of a given a"""
    return a*a

found = False
limit = 1000
for i in range(1,limit,1):
    for j in range(i+1,limit,1):
        for k in range(j+1,limit,1):
            if check_sum(i,j,k,limit) and (find_square(i) + find_square(j) == find_square(k)):
                found = True
                break
        if found:
            break
    if found:
        break
print(i*j*k)
