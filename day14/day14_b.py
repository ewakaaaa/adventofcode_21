import os
import sys

sys.path.insert(0, os.getcwd())
from utils import read_file
import math

rules = {}

puzzle_test = read_file(14, test=False)
for line in puzzle_test:
    line = line.replace("\n", "")
    if "->" in line:
        key, value = line.split(" -> ")
        rules[key] = value
    else:
        if line:
            start = line


def make_pair(start):
    pair_dict = {}
    for i in range(0, len(start) - 1):
        pair = start[i : i + 2]
        if pair in pair_dict:
            pair_dict[pair] = pair_dict[pair] + 1
        else:
            pair_dict[pair] = 1
    return pair_dict


def make_one_step(pair_dict, rules):
    new_dict = {}
    for key, value in pair_dict.items():
        new_pair_1 = key[0] + rules[key]
        new_pair_2 = rules[key] + key[1]

        for new in (new_pair_1, new_pair_2):
            if new in new_dict:
                new_dict[new] = new_dict[new] + value
            else:
                new_dict[new] = value
    return new_dict


pair = make_pair(start)
for i in range(0, 40):
    pair = make_one_step(pair, rules)

counter = {}
for key, value in pair.items():
    for letter in (key[0], key[1]):
        if letter in counter:
            counter[letter] = counter[letter] + value / 2
        else:
            counter[letter] = value / 2

max_value = 0
for values in counter.values():
    max_value = max(max_value, values)

for values in counter.values():
    min_value = min(max_value, values)

print(math.ceil(max_value) - math.ceil(min_value))
