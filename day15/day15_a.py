
import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file
import numpy as np 
from dijkstra import * 

puzzle_test = read_file(15,test = False)

# reading data
map = [] 
for line in puzzle_test:
    row = [int(item) for item in line.replace('\n','')]
    row.append(-1)
    row.insert(0, -1)
    map.append(row)

nines = [-1 for item in puzzle_test[0].replace('\n','')]
nines.append(-1)
nines.insert(0,-1)

map.append(nines)
map = np.array(map)
map = np.insert(map, 0, np.array(nines), axis=0)

map[1][1] = -1 # can't go back to start 

# creating a graph of connections between points
graph = {}
for row in range(1,map.shape[0]-1):
    for col in range(1,map.shape[1]-1):
        graph[(row,col)] = {} 
        if map[row+1][col] != -1:
            graph[(row,col)][(row+1,col)] = map[row+1][col]
        if map[row][col+1] != -1:
            graph[(row,col)][(row,col+1)] = map[row][col+1]
        if map[row-1][col] != -1:
            graph[(row,col)][(row-1,col)] = map[row-1][col]
        if map[row][col-1] != -1:
            graph[(row,col)][(row,col-1)]  = map[row][col-1] 

#meta 
graph[(map.shape[1]-2,map.shape[0]-2)] = {}


cost  = dijksta(graph,(1,1),(map.shape[0]-2,map.shape[1]-2))
print(cost)


