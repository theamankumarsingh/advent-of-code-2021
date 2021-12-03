#Day 1: Sonar Sweep
#Part 1

import sys, math

input_data=list(map(int,open(sys.argv[1], 'r').read().splitlines()))
print(input_data)

count=0

for i in range(1,len(input_data)):
    if(input_data[i]>input_data[i-1]):
        count+=1

print(count)