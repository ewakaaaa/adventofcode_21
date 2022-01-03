import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file

puzzle_test = read_file(8, test=True)
puzzle = read_file(8, test=False)


def solution(puzzle):
    result = 0
    for line in puzzle:
        line = line.split("|")[1]
        digts = line.split(" ")
        digts = [1 for item in digts if len(item.replace("\n", "")) in (2, 3, 4, 7)]
        result = result + sum(digts)
    return result


assert solution(puzzle_test) == 26

print(solution(puzzle))
