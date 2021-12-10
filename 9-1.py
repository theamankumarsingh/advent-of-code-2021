#Day 9: Smoke Basin
#Part 1

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
input_data=[list(map(int,list(x))) for x in input_data]
print(input_data)

risk=0
l=len(input_data[0])
b=len(input_data)

for i in range(b):
    for j in range(l):
        neighbors=[]
        if(i-1>=0):
            neighbors.append(input_data[i-1][j])
        if(i+1<b):
            neighbors.append(input_data[i+1][j])
        if(j-1>=0):
            neighbors.append(input_data[i][j-1])
        if(j+1<l):
            neighbors.append(input_data[i][j+1])
        risk+=input_data[i][j]+1
        for k in neighbors:
            if(input_data[i][j]>=k):
                risk-=input_data[i][j]+1
                break
                
print(risk)