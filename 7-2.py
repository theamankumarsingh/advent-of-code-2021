#Day 7: The Treachery of Whales
#Part 2

def calc_fuel(focus, input_data):
    fuel=0
    for i in input_data:
        fuel+=abs(i-focus)*(abs(i-focus)+1)//2
    return fuel

import sys, math

input_data=list(map(int,(open(sys.argv[1], 'r').read().split(','))))
print(input_data)

input_data.sort()
n=len(input_data)
fuels=[]
for focus in range(input_data[0],input_data[n-1]+1):
    fuels.append(calc_fuel(focus,input_data))

print(min(fuels))   
