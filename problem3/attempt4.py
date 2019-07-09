#!/usr/bin/env python

import math

prime_nums = [2]

def is_divisible(inpt:int, i:int) -> bool:
    return inpt%i == 0

def is_prime(inpt:int) -> bool:
    global prime_nums
    for i in prime_nums:
        if is_divisible(inpt,i):
            return False
    prime_nums.append(inpt)
    return True


num = 600851475143
max_factor = 0
num_sqrt = int(math.sqrt(num))
for i in range(3,num_sqrt,2):
    print(len(prime_nums))
    if is_prime(i) and is_divisible(num,i):
        max_factor = i

print(max_factor)

