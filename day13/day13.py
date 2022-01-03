import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file

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


def fold_along_y(points, y_line):
    points_after_fold = set()
    for point in points:
        x, y = point
        if y == y_line:
            pass
        if y > y_line:
            distance_to_y_line = y - y_line
            y = y_line - distance_to_y_line
        points_after_fold.add((x, y))
    return points_after_fold


def fold_along_x(points, x_line):
    points_after_fold = set()
    for point in points:
        x, y = point
        if x == x_line:
            pass
        if x > x_line:
            distance_to_x_line = x - x_line
            x = x_line - distance_to_x_line
        points_after_fold.add((x, y))
    return points_after_fold


# Part A
x_or_y, value = folds[0]
if x_or_y == "fold along x":
    points = fold_along_x(points, value)
if x_or_y == "fold along y":
    points = fold_along_y(points, value)
print(len(points))

# Part B
for fold in folds:
    x_or_y, value = fold
    if x_or_y == "fold along x":
        points = fold_along_x(points, value)
    if x_or_y == "fold along y":
        points = fold_along_y(points, value)

x_max = 0
y_max = 0
for point in points:
    x, y = point
    x_max = max(x, x_max)
    y_max = max(y, y_max)

instructions = [["." for i in range(x_max + 1)] for j in range(y_max + 1)]

for point in points:
    x, y = point
    instructions[y][x] = "#"

for line in instructions:
    print(line)
