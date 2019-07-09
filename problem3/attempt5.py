#!/usr/bin/env python

import math

def is_divisible(inpt:int, i:int) -> bool:
    return inpt%i == 0

def is_prime(inpt:int) -> bool:
    if inpt%2 == 0:
        return False
    inpt_sqrt = int(math.sqrt(inpt))
    prime_flag = True
    for i in range(3,inpt_sqrt,2):
        if is_divisible(inpt,i):
            prime_flag = False
            break
    return prime_flag


num = 600851475143
max_factor = 0
num_sqrt = int(math.sqrt(num))
for i in range(3,num_sqrt,2):
    if is_divisible(num,i) and is_prime(i):
        max_factor = i

print(max_factor)

