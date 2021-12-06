#Day 6: Lanternfish
#Part 1

class Fish:
    def __init__(self,incubation):
        self.incubation = incubation
    def did_reproduce(self):
        if self.incubation > 0:
            self.incubation -= 1
        elif self.incubation == 0:
            self.incubation=6
            return True
        return False

import sys, math

input_data=list(map(int,(open(sys.argv[1], 'r').read().split(','))))
print(input_data)

days=80
fishtank=[Fish(i) for i in input_data]

for i in range(days):
    newfish=[]
    for fish in fishtank:
        if fish.did_reproduce():
            newfish.append(Fish(8))
    fishtank=fishtank+newfish

print(len(fishtank))
