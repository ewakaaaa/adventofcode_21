import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file
import numpy as np
from dijkstra import *

puzzle_test = read_file(15, test=False)

# reading data
map = []
for line in puzzle_test:
    row = [int(item) for item in line.replace("\n", "")]
    map.append(row)

map = np.array(map)
map_col = map
for i in range(1, 5):
    map_col = np.concatenate((map_col, map + i), axis=1)

map_col = map_col % 9
map_col[map_col == 0] = 9

map_row = map_col
for i in range(1, 5):
    map_row = np.concatenate((map_row, map_col + i), axis=0)

map_row = map_row % 9
map_row[map_row == 0] = 9


def make_frame(map):
    row = [[0 for i in range(0, map.shape[1])]]
    map = np.append(row, map, axis=0)
    map = np.append(map, row, axis=0)
    column = np.zeros((map.shape[0], 1))
    map = np.hstack((column, map))
    map = np.hstack((map, column))
    return map


map_with_frame = make_frame(map_row)
map_with_frame[1][1] = 0  # can't go back to start

# creating a graph of connections between points
graph = {}
for row in range(1, map_with_frame.shape[0] - 1):
    for col in range(1, map_with_frame.shape[1] - 1):
        graph[(row, col)] = {}
        if map_with_frame[row + 1][col] != 0:
            graph[(row, col)][(row + 1, col)] = map_with_frame[row + 1][col]
        if map_with_frame[row][col + 1] != 0:
            graph[(row, col)][(row, col + 1)] = map_with_frame[row][col + 1]
        if map_with_frame[row - 1][col] != 0:
            graph[(row, col)][(row - 1, col)] = map_with_frame[row - 1][col]
        if map_with_frame[row][col - 1] != 0:
            graph[(row, col)][(row, col - 1)] = map_with_frame[row][col - 1]

# meta
graph[(map_with_frame.shape[1] - 2, map_with_frame.shape[0] - 2)] = {}

cost = dijksta(
    graph, (1, 1), (map_with_frame.shape[0] - 2, map_with_frame.shape[1] - 2)
)
print(cost)
