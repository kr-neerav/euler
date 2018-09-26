#!/usr/bin/env python

import math

#count number of steps in program
step = 0

#list of prime numbers as discovered. This will be used to identify new prime numbers. It has been provided some of the small prime numbers to begin with
primes = [2]


#function to identify is a number is prime
def isPrime(num):
    global step
    global primes
    if num in primes:
        return True
    for i in primes:
        step = step + 1
        if num%i == 0:
            return False
    #second loop to check if the number is prime. This will be needed incase the number is large i.e. its sqrt more than 13
    numSqrt = int(math.sqrt(num))
    for j in range(i+1, numSqrt+1):
        step = step + 1
        if num%j == 0:
            return False
    primes.append(num)
    return True

#function to identify all prime numbers less than squre root of the input numbers
def generatePrimes(num):
    global step
    numSqrt = int(math.sqrt(num))
    for i in range(2,numSqrt+1):
        temp = isPrime(num)
        step = step + 1

#function to identify all the prime factors of a number
def factors(num):
    primeFactors = []
    numSqrt = int(math.sqrt(num))   #calculate square root of a number. This will be the limit to check if it is a factor of the number
    global step
    for i in range(numSqrt,2,-1):
        step = step + 1
        if num%i == 0 and isPrime(i):
            return i

num = int(input('Enter the number :'))
#generatePrimes(num)
maxPrimeFactor = factors(num)
#print('Factors of '+str(num)+' are : '+','.join(str(x) for x in primeFactors))
print('Number of steps :' + str(step))
print('Max prime factor :' + str(maxPrimeFactor))
print(primes)
