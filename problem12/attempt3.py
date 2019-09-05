#!/usr/bin/env python3

import math

def add(a:int, b:int) -> int:
    """return the result of addition of a and b"""
    return a + b


def get_triangle_number(n:int) -> int:
    """return the n th triangle number i.e. 1 + 2 + 3 + ... + n"""
    return int(n*(n+1)/2)

def is_divisor(n:int, i:int) -> bool:
    """check if n is divisible by i"""
    return n%i == 0

def get_divisors(n:int) -> int:
    """get all divisors of number n"""
    divisors = 0
    n_sqrt = int(math.sqrt(n))
    i = 1
    while i <= n_sqrt:
        if is_divisor(n,i):
            if i == n/i:
                divisors = divisors + 1
            else:
                divisors = divisors + 2
        i = add(i,1)
    return divisors

divisors = 0
n = 0
triangle_number = 1
while(divisors < 500):
    n = n + 1
    triangle_number = get_triangle_number(n)
    divisors = get_divisors(triangle_number)

print(triangle_number)
print(n)
