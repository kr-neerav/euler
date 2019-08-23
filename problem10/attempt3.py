#!/usr/bin/env python3

import math

def is_divisible(inpt:int, i:int) -> bool:
    """check if inpt is divisible by i"""
    return inpt%i == 0
    
def is_small(a:int, b:int) -> bool:
    """check if a is smaller than or equal to b"""
    return a <= b
    
def get_probable_prime(n: int) -> [int]:
    """prime numbers always take the form of 6n-1 or 6n+1. This function generates the 
    probable prime numbers closet to n"""
    return [6*n-1, 6*n+1]
    
def is_prime(inpt:int) -> bool:
    """check if a number is prime or not"""
    inpt_sqrt = int(math.sqrt(inpt))
    i = 0
    while is_small(primes[i], inpt_sqrt):
        if is_divisible(inpt, primes[i]):
            return False
        i = i + 1
    return True

def is_large(a:int, b:int) -> bool:
    """check if a is greater than or equal to b"""
    return a>=b

primes = [2,3]
n = 1
limit = 2000000
prime1, prime2 = get_probable_prime(n)
while is_small(prime1,limit):
    if is_prime(prime1):
        primes.append(prime1)
    if is_prime(prime2) and is_small(prime2,limit):
        primes.append(prime2)
    n = n + 1
    prime1, prime2 = get_probable_prime(n)

print(sum(primes))
