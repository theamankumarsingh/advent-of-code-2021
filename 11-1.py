#Day 11: Dumbo Octopus
#Part 1

def increase_energy(l,b,input_data):
    for i in range(l):
        for j in range(b):
            input_data[i][j]+=1

def flash(i,j,l,b,input_data,flash_log):
    if(0<=i<l and 0<=j<b and (i,j) not in flash_log and input_data[i][j]>9):
        flash_log.add((i,j))
        n=0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if(not(x==0 and y==0)):
                    if(0<=i+x<l and 0<=j+y<b):
                        input_data[i+x][j+y]+=1
                    n+=flash(i+x,j+y,l,b,input_data,flash_log)
        return 1+n
    return 0

def reset_energy(input_data,flash_log):
    for i,j in flash_log:
        input_data[i][j]=0

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
input_data=[list(map(int,list(x))) for x in input_data]
print(input_data)

steps=100
flashes=0
l=len(input_data[0])
b=len(input_data)

for step in range(steps):
    flash_log=set()
    increase_energy(l,b,input_data)
    for i in range(l):
        for j in range(b):
            flashes+=flash(i,j,l,b,input_data,flash_log)
    reset_energy(input_data,flash_log)

print(flashes)