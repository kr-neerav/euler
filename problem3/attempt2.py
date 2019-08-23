#!/usr/bin/env python

import math

def is_divisible(inpt:int, i:int) -> bool:
    """check if inpt is divisible by i"""
    return inpt%i == 0

def is_prime(inpt:int) -> bool:
    """check if a number is prime or not"""
    inpt_sqrt = int(math.sqrt(inpt))
    for i in range(3,inpt_sqrt,2):
        if is_divisible(inpt,i):
            return False
    return True


num = 600851475143
max_factor = 0
num_sqrt = int(math.sqrt(num))
for i in range(3,num_sqrt,2):
    if is_prime(i) and is_divisible(num,i):
        max_factor = i

print(max_factor)

