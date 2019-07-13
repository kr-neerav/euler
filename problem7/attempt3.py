#!/usr/bin/env python

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
    l = len(primes)
    prime_num = primes[i]
    while is_small(prime_num, inpt_sqrt):
        prime_num = primes[i]
        if is_divisible(inpt, prime_num):
            return False
        #get next set of probable prime numbers
        i = i + 1
    return True


primes = [2,3]
n = 1
while len(primes) < 10001:
    prime1, prime2 = get_probable_prime(n)
    if is_prime(prime1):
        primes.append(prime1)
    if is_prime(prime2):
        primes.append(prime2)
    n = n + 1

print(primes[10000])
