#!/usr/bin/env python3


def get_triangle_number(n:int) -> int:
    """return the n th triangle number i.e. 1 + 2 + 3 + ... + n"""
    num = 0
    for i in range(1,n+1):
        num = num + i
    return num

def is_divisor(n:int, i:int) -> bool:
    """check if n is divisible by i"""
    return n%i == 0

def get_divisors(n:int) -> [int]:
    """get all divisors of number n"""
    divisors = []
    for i in range(1,n+1):
        if is_divisor(n,i):
            divisors.append(i)
    return divisors

divisors = []
n = 1
triangle_number = 1
while(len(divisors) <= 500):
    triangle_number = get_triangle_number(n)
    divisors = get_divisors(triangle_number)
    n = n + 1

print(triangle_number)
print(divisors)


