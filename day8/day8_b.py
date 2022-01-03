import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file
import numpy as np

puzzle_test = read_file(8, test=True)
puzzle = read_file(8, test=False)


def get_output_for_single_line(line):
    line = line.replace("\n", "")
    patterns, output = line.split(" | ")
    patterns = [set(item) for item in patterns.split(" ")]
    output = [set(item) for item in output.split(" ")]

    digits = {}
    for digit in patterns:
        if len(digit) == 2:
            digits[1] = digit
        if len(digit) == 4:
            digits[4] = digit
        if len(digit) == 3:
            digits[7] = digit

    output_value = ""

    for digit in output:
        if (
            len(digit) == 6
            and len(digits[4].intersection(digit)) == 3
            and len(digits[1].intersection(digit)) == 2
        ):
            output_value += "0"
        if len(digit) == 2:
            output_value += "1"
        if len(digit) == 5 and len(digits[4].intersection(digit)) == 2:
            output_value += "2"
        if len(digit) == 5 and digits[7].issubset(digit):
            output_value += "3"
        if len(digit) == 4:
            output_value += "4"
        if (
            len(digit) == 5
            and len(digits[4].intersection(digit)) == 3
            and len(digits[1].intersection(digit)) == 1
        ):
            output_value += "5"
        if len(digit) == 6 and len(digits[1].intersection(digit)) == 1:
            output_value += "6"
        if len(digit) == 3:
            output_value += "7"
        if len(digit) == 7:
            output_value += "8"
        if len(digit) == 6 and digits[4].issubset(digit):
            output_value += "9"
    return int(output_value)


puzzle_result = []
for line in puzzle:
    puzzle_result.append(get_output_for_single_line(line))

print(sum(puzzle_result))
