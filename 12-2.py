#Day 12: Passage Pathing
#Part 2

class Cave:
    def __init__(self,name,links=[]):
        self.name = name
        self.links = links
    def add_link(self,link):
        if link not in self.links:
            self.links.append(link)
    def print(self):
        print(self.name,self.links)

def get_paths(caves,obj,path,flag):
    if obj.name == 'end':
        if path not in all_paths:
            all_paths.append(path)
        return
    if obj.name == 'start':
        path.append(obj.name)
    for link in obj.links:
        old_flag=flag
        if link=='start':
            continue
        if link.islower() and link in path:
            if flag:
                continue
            else:
                flag=True
        path.append(link)
        get_paths(caves,caves[link],path.copy(),flag)
        path.pop()
        flag=old_flag

import sys, math, time

input_data=list(open(sys.argv[1], 'r').read().splitlines())
input_data=[x.split('-') for x in input_data]
print(input_data)

caves = dict()
all_paths = []

for connection in input_data:
    if connection[0] in caves.keys():
        obj=caves[connection[0]]
        obj.add_link(connection[1])
    else:
        caves[connection[0]]=Cave(connection[0],[connection[1]])

    if connection[1] in caves.keys():
        obj=caves[connection[1]]
        obj.add_link(connection[0])
    else:
        caves[connection[1]]=Cave(connection[1],[connection[0]])

get_paths(caves,caves['start'],[],False)
print(len(all_paths))