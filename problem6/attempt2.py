#!/usr/bin/env python

def square(num:int) -> int:
    """return the square of num"""
    return num*num

def sum_of_squares(num:int) -> int:
    """return sum of squres of numbers from 1 to num"""
    return int(num*(num+1)*(2*num+1)/6)

def square_of_sum(num:int) -> int:
    """return the square of sum of numbers from 1 to num"""
    return int((num*(num+1)/2)*(num*(num+1)/2))

num = 100

print(square_of_sum(num) - sum_of_squares(num))
