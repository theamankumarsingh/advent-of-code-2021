#Day 5: Hydrothermal Venture
#Part 2

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

maximum=0
coord=[]
for l in input_data:
    l=l.split('->')
    l=list(map(int, l[0].split(',')+l[1].split(',')))
    if(maximum<max(l)):
        maximum=max(l)
    coord.append(l)
xyplane=[[0 for i in range(maximum+1)] for j in range(maximum+1)]

for xy in coord:
    if(xy[0]==xy[2]):
        for y in range(min(xy[1],xy[3]),max(xy[1],xy[3])+1):
            xyplane[xy[0]][y]+=1
    if(xy[1]==xy[3]):
        for x in range(min(xy[0],xy[2]),max(xy[0],xy[2])+1):
            xyplane[x][xy[1]]+=1
    if(abs(xy[2]-xy[0])==abs(xy[3]-xy[1])):
        for t in range(abs(xy[2]-xy[0])+1):
            xyplane[xy[0]+t*(1 if xy[2]>xy[0] else -1)][xy[1]+t*(1 if xy[3]>xy[1] else -1)]+=1
count=0
for i in xyplane:
    for j in i:
        if(j>1):
            count+=1
print(count)