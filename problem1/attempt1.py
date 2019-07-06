#!/usr/bin/env python

upper_limit = 1000
nums = []
div1 = 3
div2 = 5

for i in range(upper_limit):
    if  i%div1 == 0 or i%div2 == 0:
        nums.append(i)
print(sum(nums))
