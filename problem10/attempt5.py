#!/usr/bin/env python3

limit = 2000000
inpt_list = list(range(limit + 1))

def get_next_id(idx:int) -> int:
    """get the id of the next non zero number from inpt_list starting at idx"""
    i = idx
    while i < limit:
        if inpt_list[i]>0:
            break
        i = i + 1
    return i

def set_idx(idx:int) -> None:
    """set the value at idx to 0 in input list. This function will be used to
    track the number of operations"""
    global inpt_list
    inpt_list[idx] = 0

def mark_non_prime(val:int) -> None:
    """mark all multiples of val as 0 as they are non prime"""
    tmp = val + val
    while tmp < limit:
        set_idx(tmp)
        tmp = tmp + val

set_idx(1)
prime = 2
while prime < limit:
    mark_non_prime(prime)
    prime = get_next_id(prime+1)

inpt_list.pop()
print(sum(inpt_list))

