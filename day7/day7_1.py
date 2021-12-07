import os
import statistics
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file

puzzle = read_file(7)
crabs = [int(item) for item in puzzle[0].split(',')]

print(sum([abs(item - statistics.median(crabs)) for item in crabs]))


