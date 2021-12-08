#Day 8: Seven Segment Search
#Part 2

def decipher(learning_data,key):
    key[1]=learning_data[0]
    key[4]=learning_data[2]
    key[7]=learning_data[1]
    key[8]=learning_data[9]
    for i in learning_data[6:9]:
        if set(key[4]) <= set(i):
            key[9]=i
        elif set(key[1]) <= set(i):
            key[0]=i
        else:
            key[6]=i
    for i in learning_data[3:6]:
        if (set(key[1]) <= set(i)):
            key[3]=i
        elif (set(i) <= set(key[6])):
            key[5]=i
        else:
            key[2]=i

def decode(code,key):
    num=0
    for i in code:
        for k,v in key.items():
            if set(i) == set(v):
                num=num*10+k
    return num

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
input_data=[l.split('|') for l in input_data]
input_data=[l[0].split()+l[1].split() for l in input_data]
print(input_data)

sum_of_nums=0

for l in input_data:
    key={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
    learning_data=l[:10]
    code=l[10:]
    learning_data.sort(key=len)
    decipher(learning_data,key)
    sum_of_nums+=decode(code,key)

print(sum_of_nums)