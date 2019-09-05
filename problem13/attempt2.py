#!/usr/bin/env python3

f = open('input.txt','r')

inpt = f.readlines()


s = 0
for num_str in inpt:
    num = int(num_str[:13])
    s = s + num

print(s)
print(str(s)[:10])

