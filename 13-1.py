#Day 13: Transparent Origami
#Part 1

import sys, math, time

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

dotmap=[]
instructions=[]
flag=0
for i in input_data:
    if i=='':
        flag=1
        continue
    if flag:
        instructions.append((i[11],int(i[13:])))
    else:
        dotmap.append(tuple(map(int,i.split(','))))

for instruction in instructions:
    new_dotmap=[k for k in dotmap]
    if instruction[0]=='y':
        for coord in dotmap:
            if(coord[1]>=instruction[1]):
                new_dotmap.remove(coord)
                new_coord=(coord[0],2*instruction[1]-coord[1])
                if(new_coord not in dotmap and new_coord!=coord):
                    new_dotmap.append(new_coord)
    if instruction[0]=='x':
        for coord in dotmap:
            if(coord[0]>=instruction[1]):
                new_dotmap.remove(coord)
                new_coord=(2*instruction[1]-coord[0],coord[1])
                if(new_coord not in dotmap and new_coord!=coord):
                    new_dotmap.append(new_coord)              
    dotmap=[k for k in new_dotmap]
    break

print(len(dotmap))