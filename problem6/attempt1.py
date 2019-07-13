#!/usr/bin/env python

def square(num:int) -> int:
    """return the square of num"""
    return num*num

def sum_of_squares(num:int) -> int:
    """return sum of squres of numbers from 1 to num"""
    s = 0
    for i in range(num):
        s = s + square(i)
    return s

def square_of_sum(num:int) -> int:
    """return the square of sum of numbers from 1 to num"""
    s = 0
    for i in range(num):
        s = s + i
    return square(s)

num = 101

print(square_of_sum(num) - sum_of_squares(num))
