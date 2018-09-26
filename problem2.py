#! /usr/bin/env python

#count number of steps
step = 0

#fibonacci limit
limit = 4000000

#fibonacci initialization
a = 1
b = 1
c = a+b
sumFibo = 0 #initialized the variable that will capture the sum of even valued terms 


#loop for fibonacci series
while c < limit:
    #if c%2 == 0:
    sumFibo = sumFibo + c
    a = b + c
    b = c + a
    c = a + b
    step = step + 1

#print output
print('Sum of even valued terms: ' + str(sumFibo))
print('Number of steps: ' + str(step))
