#!/usr/bin/env python

import math

#count number of steps in program
step = 0

num = int(input('Enter the number :'))
primeFactors = []
evenFlag = False
while num%2 == 0:
    num = num/2
    step =  step + 1
    evenFlag = True
if evenFlag:
    primeFactors.append(2)
factor = 3

while num > 1:
    step = step + 1
    factorFlag = False
    while num%factor == 0:
        num = num/factor
        step = step + 1
        factorFlag = True
    if factorFlag:
        primeFactors.append(factor)
    factor = factor + 2
print('Number of steps :' + str(step))
print('Max prime factor :' + str(max(primeFactors)))
print(primeFactors)
