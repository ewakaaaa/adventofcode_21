import os
import sys

sys.path.insert(0, os.getcwd()) 
from utils import read_file

def step_cost(up,to):
    distanse = abs(up-to)
    return sum([item for item in range(1,distanse+1)]) 

assert step_cost(16,5) == 66

puzzle = read_file(7)
crabs = [int(item) for item in puzzle[0].split(',')]

possible_position = [item for item in range(min(crabs), max(crabs)+1 )]
cheapest_possible = 1000000000 

for position in possible_position:
    fuel = []
    for item in crabs: 
        fuel.append(step_cost(position,item))
    if cheapest_possible > sum(fuel):
        cheapest_possible = sum(fuel)

print(cheapest_possible)




