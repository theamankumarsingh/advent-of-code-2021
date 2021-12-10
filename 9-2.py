#Day 9: Smoke Basin
#Part 2

def find_basin(i,j,b,l,input_data,basin):
    if((i,j)not in basin):
        basin.add((i,j))
        if(i-1>=0):
            if(input_data[i-1][j]>input_data[i][j] and input_data[i-1][j]!=9):
                find_basin(i-1,j,b,l,input_data,basin)
        if(i+1<b):
            if(input_data[i+1][j]>input_data[i][j] and input_data[i+1][j]!=9):
                find_basin(i+1,j,b,l,input_data,basin)
        if(j-1>=0):
            if(input_data[i][j-1]>input_data[i][j] and input_data[i][j-1]!=9):
                find_basin(i,j-1,b,l,input_data,basin)
        if(j+1<l):
            if(input_data[i][j+1]>input_data[i][j] and input_data[i][j+1]!=9):
                find_basin(i,j+1,b,l,input_data,basin)
        return len(basin)

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
input_data=[list(map(int,list(x))) for x in input_data]
print(input_data)

l=len(input_data[0])
b=len(input_data)
basins=[]
for i in range(b):
    for j in range(l):
        neighbors=[]
        basin=set()
        if(i-1>=0):
            neighbors.append(input_data[i-1][j])
        if(i+1<b):
            neighbors.append(input_data[i+1][j])
        if(j-1>=0):
            neighbors.append(input_data[i][j-1])
        if(j+1<l):
            neighbors.append(input_data[i][j+1])
        is_low_point=True
        for k in neighbors:
            if(input_data[i][j]>=k):
                is_low_point=False
        if(is_low_point):
            basins.append(find_basin(i,j,b,l,input_data,basin))
basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])