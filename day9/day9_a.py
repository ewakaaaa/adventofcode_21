import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file
import numpy as np 

puzzle_test = read_file(9,test = False)

map = [] 
for line in puzzle_test:
    row = [int(item) for item in line.replace('\n','')]
    row.append(row[-1]+1)
    row.insert(0, row[0]+1)
    map.append(row)

line_0 = [int(item) +1 for item in puzzle_test[0].replace('\n','')]
line_0.append(10)
line_0.insert(0,10)
line_n = [int(item) +1 for item in puzzle_test[-1].replace('\n','')]
line_n.append(10)
line_n.insert(0,10)

map.append(line_n)
map = np.array(map)
map = np.insert(map, 0, np.array(line_0), axis=0)


print(map)
risk = 0 

for row in range(1,map.shape[0]-1):
    for col in range(1,map.shape[1]-1):
        point = map[row][col]
        if map[row+1][col] > point:
            if map[row][col+1] > point:
                if map[row-1][col] > point:
                    if map[row][col-1] > point:
                        risk = risk + point + 1  

print(risk)

