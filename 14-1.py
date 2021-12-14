#Day 14: Extended Polymerization
#Part 1

def subtraction(polymer):
    max_freq=min_freq=polymer.count(polymer[0])
    for ch in polymer:
        ch_freq = polymer.count(ch)
        if(ch_freq > max_freq):
            max_freq=ch_freq
        if(ch_freq < min_freq):
            min_freq=ch_freq
    return max_freq-min_freq

import sys, math, time

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

polymer=list(input_data[0])
rules={}
for i in input_data[2:]:
    key,value=i.split(' -> ')
    rules[key]=value

steps=10
for k in range(steps):
    new_polymer=[x for x in polymer]
    j=1
    for i in range(1,len(polymer)):
        pair=polymer[i-1]+polymer[i]
        if pair in rules.keys():
            new_polymer.insert(j,rules[pair])
            j+=2
        else:
            j+=1
    polymer=[x for x in new_polymer]

print(subtraction(polymer))