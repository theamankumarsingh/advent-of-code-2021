#Day 4: Giant Squid
#Part 1

class Board:
    def __init__(self,board):
        self.board=board
    def check_bingo(self):
        for i in self.board:
            if i.count(1)==5:
                return True
        for i in range(5):
            if self.board[0][i]==1 and self.board[1][i]==1 and self.board[2][i]==1 and self.board[3][i]==1 and self.board[4][i]==1:
                return True
        return False

    def insert(self,r,c):
        self.board[r][c]=1
        return self.check_bingo()

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)

callout=list(map(int,input_data[0].split(',')))

elements=dict()
n=0
r=0

for i in range(2,len(input_data)):
    if input_data[i]=='':
        n+=1
        r=0
    else:
        c=0
        data=list(map(int,input_data[i].split()))
        for k in data:
            if k in callout:
                if k not in elements:
                    elements[k]=[[n,r,c]]
                else:
                    elements[k].append([n,r,c])
            c+=1
        r+=1

objlist=[]
for i in range(n+1):
    objlist.append(Board([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))

flag=1

for i in callout:
    coordinate=elements[i]
    for j in coordinate:
        if(objlist[j[0]].insert(j[1],j[2]) and flag):
            winning_number=i
            winning_board=j[0]
            flag=0
            callout=callout[:callout.index(i)+1]
            break
    if(flag==0):
        break

s=0
num=0

for i in range(2,len(input_data)):
    if input_data[i]=='':
        num+=1
        continue
    if num==winning_board:
        data=list(map(int,input_data[i].split()))
        for k in data:
            if k not in callout:
                s+=k

print(s*winning_number)

