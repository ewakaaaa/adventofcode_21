import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file
import numpy as np
import math

puzzle_test = read_file(9,test = False)

map = [] 
for line in puzzle_test:
    row = [int(item) for item in line.replace('\n','')]
    row.append(9)
    row.insert(0, 9)
    map.append(row)

nines = [9 for item in puzzle_test[0].replace('\n','')]
nines.append(9)
nines.insert(0,9)

map.append(nines)
map = np.array(map)
map = np.insert(map, 0, np.array(nines), axis=0)

graph = {}
for row in range(1,map.shape[0]-1):
    for col in range(1,map.shape[1]-1):
        where_can_go = [] 
        if map[row][col]!= 9: 
            if map[row+1][col] != 9:
                where_can_go.append((row+1,col))
            if map[row][col+1] != 9:
                where_can_go.append((row,col+1))
            if map[row-1][col] != 9:
                where_can_go.append((row-1,col))
            if map[row][col-1] != 9:
                where_can_go.append((row,col-1))
            graph[(row,col)] = where_can_go

pools_centrum = [] 
for row in range(1,map.shape[0]-1):
    for col in range(1,map.shape[1]-1):
        point = map[row][col]
        if map[row+1][col] > point:
            if map[row][col+1] > point:
                if map[row-1][col] > point:
                    if map[row][col-1] > point:
                        pools_centrum.append((row,col))

pool_sizes = [] 
for centrum in pools_centrum: 
    pool_size = [centrum] 
    visited = [centrum]
    pool_size.extend(graph[centrum])
    for i in pool_size:
        if i in visited:
            pass 
        else: 
            visited.append(i)
            pool_size.extend(graph[i])
    pool_sizes.append(len(set(pool_size)))

print(math.prod(sorted(pool_sizes,reverse=True)[:3])) 
                   







