#Day 10: Syntax Scoring
#Part 2

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
reward={'(':1,'[':2,'{':3,'<':4}
scores=[]

for line in input_data:
    stack=[]
    corrupt=check(line,stack,opening,closing)
    if(corrupt=='' and len(stack)!=0):
        score=0
        stack.reverse()
        for i in stack:
            score=score*5+reward[i]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])
