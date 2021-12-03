#Day 2: Dive!
#Part 2

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

f=d=a=0
for i in input_data:
    direction,num=i.split()
    if direction=='forward':
        f+=int(num)
        d+=a*int(num)
    if direction=='down':
        a+=int(num)
    if direction=='up':
        a-=int(num)

print(f*d)