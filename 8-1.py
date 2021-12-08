#Day 8: Seven Segment Search
#Part 1

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
input_data=[l.split('|') for l in input_data]
input_data=[l[0].split()+l[1].split() for l in input_data]
print(input_data)

count=0

for l in input_data:
    for i in range(10,len(l)):
        if len(l[i]) in [2,4,3,7]:
            count+=1

print(count)