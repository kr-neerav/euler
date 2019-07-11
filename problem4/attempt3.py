#!/usr/bin/env python

def is_large(a:int, b:int) -> bool:
    """check if a is greater than or equal to b"""
    return a>=b

def get_remainder(n:int, d:int) -> int:
    """return the remainder when n is divided by d"""
    return n%d

def is_palindrome(num:int) -> bool:
    """check if a number is palindrome by reversing the number"""
    rev = 0
    temp = num
    while temp!= 0:
        rev = rev*10 + get_remainder(temp, 10)
        temp = int(temp/10)
    return num == rev

num1 = 999
num2 = 999
max_palindrome = 0
for i in range(num1,99,-1):
    for j in range(num2,99,-1):
        if is_large(i*j, max_palindrome) and is_palindrome(i*j):
            max_palindrome = i*j

print(max_palindrome)
