import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file

close_to_open = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

score = {
    "0": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


test_line_1 = [
    "{",
    "(",
    "[",
    "(",
    "<",
    "{",
    "}",
    "[",
    "<",
    ">",
    "[",
    "]",
    "}",
    ">",
    "{",
    "[",
    "]",
    "{",
    "[",
    "(",
    "<",
    "(",
    ")",
    ">",
]
test_line_0 = [
    "{",
    "(",
    "[",
    "{",
    "{",
    "}",
    "}",
    "[",
    "<",
    "[",
    "[",
    "[",
    "<",
    ">",
    "{",
    "}",
    "]",
    "]",
    "]",
    ">",
    "[",
    "]",
]


def find_corrupted(line):
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
                return item_close
    return "0"


wrong_close = []
for line in read_file(10, test=True):
    line = [item for item in line.replace("\n", "")]
    wrong_close.append(score[find_corrupted(line)])

print(sum(wrong_close))
