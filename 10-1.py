#Day 10: Syntax Scoring
#Part 1

def check(line,stack,opening,closing):
    for i in line:
        if i in opening:
            stack.append(i)
        if i in closing:
            if(stack[-1]==opening[closing.index(i)]):
                stack.pop()
            else:
                return i
    return ''

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

opening=['(','[','{','<']
closing=[')',']','}','>']
reward={')':3,']':57,'}':1197,'>':25137}
score=0

for line in input_data:
    stack=[]
    corrupt=check(line,stack,opening,closing)
    if(corrupt!=''):
        score+=reward[corrupt]

print(score)
