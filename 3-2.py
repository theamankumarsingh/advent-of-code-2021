#Day 3: Binary Diagnostic
#Part 2

def remove_elements(arr,criteria):
    for i in range(len(arr)-1,-1,-1):
        if not criteria(arr[i]):
            del arr[i]

import sys, math

input_data=list(open(sys.argv[1], 'r').read().splitlines())
print(input_data)
o2=input_data.copy()
co2=input_data.copy()

for i in range(len(o2[0])):
    if(len(o2)==1):
        break
    count=0
    for j in range(len(o2)):
        if(o2[j][i]=="1"):
            count+=1
    if(count>=(len(o2)-count)):
        remove_elements(o2,lambda x: x[i]=="1")
    else:
        remove_elements(o2,lambda x: x[i]=="0")

for i in range(len(co2[0])):
    if(len(co2)==1):
        break
    count=0
    for j in range(len(co2)):
        if(co2[j][i]=="0"):
            count+=1
    if(count>(len(co2)-count)):
        remove_elements(co2,lambda x: x[i]=="1")
    else:
        remove_elements(co2,lambda x: x[i]=="0")

print(int(o2[0],2)*int(co2[0],2))