#Day 2: Dive!
#Part 1

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

f=d=0
for i in input_data:
    direction,num=i.split()
    if direction=='forward':
        f+=int(num)
    if direction=='down':
        d+=int(num)
    if direction=='up':
        d-=int(num)

print(f*d)