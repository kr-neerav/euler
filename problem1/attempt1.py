#!/usr/bin/env python3

def is_divisible(i:int, j:int) -> bool:
    """return if i is divisible by j"""
    return i%j == 0

upper_limit = 1000
nums = []
div1 = 3
div2 = 5

for i in range(upper_limit):
    if  is_divisible(i, div1) or is_divisible(i, div2):
        nums.append(i)
print(sum(nums))
