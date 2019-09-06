#!/usr/bin/env python3

series_end = 1
limit = 1000000
series_len = {}

def get_next(n:int) -> int:
    """get the next number in series"""
    if n%2 == 0:
        return int(n/2)
    return 3*n + 1

def get_series_len(n:int) -> int:
    """get the length of Collatz series starting at n"""
    global series_len
    if n == 1:
        return 1
    if str(n) in series_len.keys():
        return series_len[str(n)]
    if n%2 == 0:
        return 1 + get_series_len(int(n/2))
    else:
        return 1 + get_series_len(3*n + 1)


max_series_len = 0
max_series_n = 0
n = 1
while n < limit :
    l = get_series_len(n)
    series_len[str(n)] = l
    if max_series_len < l:
        max_series_len = l
        max_series_n = n
    n = n + 1

print(max_series_len)
print(max_series_n)
