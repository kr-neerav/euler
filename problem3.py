#!/usr/bin/env python

import math

#count number of steps in program
step = 0

#function to identify is a number is prime
def isPrime(num):
    numSqrt = int(math.sqrt(num))   #calculate square root of a number. this will be the limit to check if a number is prime or now
    global step
    for i in range(2,numSqrt+1):
        step = step + 1
        if num%i ==0:
            return False
    return True

#function to identify all the prime factors of a number
def factors(num):
    primeFactors = []
    numSqrt = int(math.sqrt(num))   #calculate square root of a number. This will be the limit to check if it is a factor of the number
    global step
    for i in range(2, numSqrt+1):
        step = step + 1
        if num%i == 0 and isPrime(i):
            primeFactors.append(i)
    return primeFactors

num = int(input('Enter the number :'))
primeFactors = factors(num)
print('Factors of '+str(num)+' are : '+','.join(str(x) for x in primeFactors))
print('Number of steps :' + str(step))


