import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file
import numpy as np

puzzle_test = read_file(11,test = True)

map = [] 
for line in puzzle_test:
    row = [int(item) for item in line.replace('\n','')]
    row.append(-1)
    row.insert(0, -1)
    map.append(row)

frame = [-1 for item in puzzle_test[0].replace('\n','')]
frame.append(-1)
frame.insert(0,-1)

map.append(frame)
map = np.array(map)
map = np.insert(map, 0, np.array(frame), axis=0)

def make_one_step (map): 
    # the energy level of each octopus increases by 1: 
    map[1:map.shape[0]-1,1:map.shape[1]-1] +=1 

    # Then, any octopus with an energy level greater than 9 flashes. 
    result = np.where(map[1:map.shape[0]-1,1:map.shape[1]-1] > 9) 

    coordinates = set(zip(result[0]+1, result[1]+1))
    flashes = set() #(An octopus can only flash at most once per step.)

    while (len(coordinates) > 0) and (not coordinates.issubset(flashes)): 
        for cord in coordinates-flashes:
            # This increases the energy level of all adjacent octopuses by 1: 
            row = cord[0]
            col = cord[1]

            map[row-1][col-1] += 1
            map[row-1][col] += 1
            map[row-1][col+1] += 1
            map[row][col-1] += 1
            
            map[row][col+1] += 1
            map[row+1][col-1] += 1
            map[row+1][col] += 1
            map[row+1][col+1] += 1
            flashes.add(cord)

            result = np.where(map[1:map.shape[0]-1,1:map.shape[1]-1] > 9) 
            coordinates = set(zip(result[0]+1, result[1]+1))

    for cord in flashes: 
        row = cord[0]
        col = cord[1]
        map[row][col] = 0  
    return map , len(flashes)

# Part A 
total_flashes = [] 
for i in range(0,100):
    map, flashes = make_one_step (map) 
    total_flashes.append(flashes)

print(sum(total_flashes))

# Part B 
flashes = 0 
step = 0
while flashes != (map.shape[0]-2) * (map.shape[1]-2):
    map, flashes = make_one_step (map) 
    step += 1 

print(step)


