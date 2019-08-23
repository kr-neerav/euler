#!/usr/bin/env python

def sum_of_series(upper_limit:int, factor:int) -> int:
    s = int(upper_limit/factor)
    return int(factor*s*(s+1)/2)

upper_limit = 999
div1 = 3
div2 = 5

output = sum_of_series(upper_limit, div1) + sum_of_series(upper_limit, div2) - sum_of_series(upper_limit, div1*div2)

print(output)
