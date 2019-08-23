#!/usr/bin/env python

import math

def is_divisible(inpt:int, i:int) -> bool:
    """check if inpt is divisible by i"""
    return inpt%i == 0

def get_probable_prime(n: int) -> [int]:
    """prime numbers always take the form of 6n-1 or 6n+1. This function generates the 
    probable prime numbers closet to n"""
    return [6*n-1, 6*n+1]

def is_small(a:int, b:int) -> bool:
    """check if a is smaller than or equal to b"""
    return a <= b

def is_prime(inpt:int) -> bool:
    """check if a number is prime or not"""
    inpt_sqrt = int(math.sqrt(inpt))
    n = 1
    prime1, prime2 = get_probable_prime(n)
    # loop to check all numbers of the format 6n-1 and 6n+1 less than inpt_sqrt which divide inpt
    while is_small(prime2, inpt_sqrt) or is_small(prime1, inpt_sqrt):
        if is_divisible(inpt, prime1) or is_divisible(inpt, prime2):
            return False
        #get next set of probable prime numbers
        n = n + 1
        prime1, prime2 = get_probable_prime(n)
    return True

def get_prime_factors(inpt:int) -> [int]:
    """generate all prime factors of a given number"""
    # for 2 and 3 manual check is to be performed as they are not in the format of 6n-1 and 6n+1
    prime_factors = []
    if is_divisible(num,2):
        prime_factors.append(2)
    if is_divisible(num,3):
        prime_factors.append(3)
    inpt_sqrt = int(math.sqrt(inpt))
    #generate first set of probable prime numbers
    n = 1
    prime1, prime2 = get_probable_prime(n)
    #loop to check for all numbers less than inpt_sqrt of the format 6n-1 and 6n+1 which are prime and divide inpt
    while is_small(prime1, inpt_sqrt) or is_small(prime2, inpt_sqrt):
        if is_divisible(inpt, prime1) and is_prime(prime1):
            prime_factors.append(prime1)
        if is_divisible(inpt, prime2) and is_prime(prime2) and is_small(prime2, inpt_sqrt):
            prime_factors.append(prime2)
        #generate next set of probable prime numbers
        n = n + 1
        prime1, prime2 = get_probable_prime(n)
    return prime_factors


num = 600851475143
print(max(get_prime_factors(num)))

