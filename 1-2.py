#Day 1: Sonar Sweep
#Part 2

import sys, math

input_data=list(map(int,open(sys.argv[1], 'r').read().splitlines()))
print(input_data)

count=0

for i in range(3,len(input_data)):
    if(input_data[i]>input_data[i-3]):
        count+=1

print(count)