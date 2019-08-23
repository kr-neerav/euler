#!/usr/bin/env python3

import math

def is_divisible(inpt:int, i:int) -> bool:
    """check if inpt is divisible by i"""
    return inpt%i == 0

def is_prime(inpt:int) -> bool:
    """check if a number is prime or not"""
    inpt_sqrt = int(math.sqrt(inpt))
    prime_flag = True
    for i in range(2,inpt_sqrt):
        if is_divisible(inpt,i):
            prime_flag = False
            break
    return prime_flag


num = 600851475143
max_factor = 0
num_sqrt = int(math.sqrt(num))
for i in range(2,num_sqrt):
    if is_prime(i) and is_divisible(num,i):
        max_factor = i

print(max_factor)

