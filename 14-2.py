#Day 14: Extended Polymerization
#Part 2 

import sys, math, time

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

pairs={}
rules={}
freq={}
for i in range(1,len(input_data[0])):
    pair=input_data[0][i-1]+input_data[0][i]
    if pair in pairs.keys():
        pairs[pair] += 1
    else:
        pairs[pair] = 1
for i in input_data[2:]:
    key,value=i.split(' -> ')
    rules[key]=value
for i in input_data[0]:
    if i in freq.keys():
        freq[i]+=1
    else:
        freq[i]=1

steps=40
for i in range(steps):
    new_pairs={}
    for j in pairs.keys():
        ch=rules[j]
        if ch in freq.keys():
            freq[ch]+=pairs[j]
        else:
            freq[ch]=pairs[j]
        pair1,pair2=j[0]+ch,ch+j[1]
        if pair1 in new_pairs.keys():
            new_pairs[pair1]+=pairs[j]
        else:
            new_pairs[pair1]=pairs[j]
        if pair2 in new_pairs.keys():
            new_pairs[pair2]+=pairs[j]
        else:
            new_pairs[pair2]=pairs[j]
    pairs=new_pairs.copy()

values=freq.values()
print(max(values)-min(values))