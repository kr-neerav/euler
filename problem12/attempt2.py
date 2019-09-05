#!/usr/bin/env python3

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
    for i in range(1,int(n/2)+1):
        if is_divisor(n,i):
            divisors = divisors + 1
    return divisors + 1

divisors = 0
n = 0
triangle_number = 1
while(divisors < 500):
    n = n + 1
    triangle_number = get_triangle_number(n)
    divisors = get_divisors(triangle_number)
    if is_divisor(n, 100):
        print(n)



print(triangle_number)
print(n)
print(len(divisors))
