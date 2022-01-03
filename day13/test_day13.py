import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file
from day13 import fold_along_y

def test_puzzle():
    puzzle_test = read_file(13, test=False)
    points = set()
    folds = []
    for line in puzzle_test:
        line = line.replace("\n", "")
        if "," in line:
            x, y = line.split(",")
            points.add((int(x), int(y)))
        else:
            x_or_y, value = line.split("=")
            folds.append((x_or_y, int(value)))

    assert len(fold_along_y(points,7)) == 879