import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file
from day8_b import get_output_for_single_line


def test_get_output_for_single_line():
    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    assert get_output_for_single_line(line) == 5353


def test_puzzle():
    puzzle_test = read_file(8, test=True)
    puzzle_test_result = []
    for line in puzzle_test:
        puzzle_test_result.append(get_output_for_single_line(line))
    assert puzzle_test_result == [
        8394,
        9781,
        1197,
        9361,
        4873,
        8418,
        4548,
        1625,
        8717,
        4315,
    ]
