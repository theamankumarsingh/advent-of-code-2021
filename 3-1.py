#Day 3: Binary Diagnostic
#Part 1

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

gamma=""
epsilon=""

for i in range(len(input_data[0])):
    count=0
    for j in range(len(input_data)):
        if(input_data[j][i]=="1"):
            count+=1
    if(count>(len(input_data)-count)):
        gamma+=("1")
        epsilon+=("0")
    else:
        gamma+=("0")
        epsilon+=("1")

print(int(gamma,2)*int(epsilon,2))