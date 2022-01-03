import os
import sys
sys.path.insert(0, os.getcwd())
from utils import read_file
import statistics

open_to_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

close_to_open = {v: k for k, v in open_to_close.items()}

score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def find_incomplete(line):
    line_copy = line.copy()
    for i, item_close in enumerate(line):
        if item_close in close_to_open.keys():
            opens_line = line_copy[:i]
            opens_line_without_0 = [item for item in opens_line if item != "0"]
            if close_to_open[item_close] == opens_line_without_0[-1]:
                index_open = (
                    len(opens_line)
                    - opens_line[::-1].index(close_to_open[item_close])
                    - 1
                )
                line_copy[index_open] = "0"
                line_copy[i] = "0"
            else:
                return "1"
    return line_copy


def calculate_score(line_copy):
    total_score = 0
    line_without_0 = [item for item in line_copy if item != "0"]
    line_without_0.reverse()
    for item in line_without_0:
        total_score = total_score * 5 + score[item]
    return total_score


scores = []
for line in read_file(10, test=False):
    line = [item for item in line.replace("\n", "")]
    if find_incomplete(line) != "1":
        scores.append(calculate_score(find_incomplete(line)))

print(statistics.median(scores))
