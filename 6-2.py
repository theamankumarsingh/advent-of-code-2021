#Day 6: Lanternfish
#Part 2

import sys, math

input_data=list(map(int,(open(sys.argv[1], 'r').read().split(','))))
print(input_data)

days=256
reproduction_waitlist=[0]*9

for i in input_data:
    reproduction_waitlist[i]+=1

for i in range(days):
    a=reproduction_waitlist.pop(0)
    reproduction_waitlist[6]+=a
    reproduction_waitlist.append(a)

print(sum(reproduction_waitlist))
