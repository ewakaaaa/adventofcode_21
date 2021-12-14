import os
import sys
sys.path.insert(0, os.getcwd()) 
from utils import read_file
from collections import Counter 

rules = {}

puzzle_test = read_file(14,test = False)
for line in puzzle_test:
    line = line.replace("\n",'')
    if "->" in line: 
        key,value = line.split(" -> ")
        rules[key] = value
    else: 
        if line:
            start = line

def make_one_step(start,rules):
    end = start[0]
    for i in range(0,len(start)-1):
        pair = start[i:i+2]
        if pair in rules:
            end = end + rules[pair]
            end = end + start[i+1]
    return end


# assert make_one_step(start,rules) == 'NCNBCHB'
# assert make_one_step('NCNBCHB',rules) == 'NBCCNBBBCBHCB'

for i in range(0,40):
    start = make_one_step(start,rules)

letters = Counter(start).most_common()
max_l, max = letters[0]
min_l , min = letters[-1]

print(max-min)
