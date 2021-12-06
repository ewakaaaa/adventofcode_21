from collections import Counter 

file_name = '/Users/ewasu/adventofcode_21/day6/puzzle.txt'
puzzle = open(file_name,'r') 
lines = puzzle.readlines() 

fish = [int(item) for item in lines[0].split(',')]
fish_dict = dict(Counter(fish)) 

for i in range (0,9):
    if not i in fish_dict: 
        fish_dict[i] = 0 

day = 0
while day != 256: 
    new_fish = fish_dict[0]
    for i in range(0,8):
        fish_dict[i] = fish_dict[i+1] 
    fish_dict[8] = new_fish 
    fish_dict[6] = new_fish + fish_dict[6] 
    day = day + 1 

print(sum(fish_dict.values()))