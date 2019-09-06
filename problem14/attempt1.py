#!/usr/bin/env python3

series_end = 1
limit = 999999


def get_next(n:int) -> int:
    """get the next number in series"""
    if n%2 == 0:
        return int(n/2)
    return 3*n + 1

def get_series_len(n:int) -> int:
    """get the length of Collatz series starting at n"""
    l = 1
    while n >1:
        n = get_next(n)
        l = l + 1
    return l

max_series_len = 0
max_series_n = 0
n = limit
while n > 0:
    l = get_series_len(n)
    if max_series_len < l:
        max_series_len = l
        max_series_n = n
    n = n - 1

print(max_series_len)
print(max_series_n)
