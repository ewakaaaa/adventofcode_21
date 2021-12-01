file_name = '/Users/ewasu/adventofcode_21/day1/puzzle.txt'
puzzle = open(file_name,'r') 

def sum_increased(puzzle):
    item_0 = 0
    counter = 0 
    for item in puzzle: 
        if int(item) > item_0:
            counter = counter + 1
        item_0 = int(item)
    return counter - 1 

print(sum_increased(puzzle))

file_name = '/Users/ewasu/adventofcode_21/day1/puzzle.txt'
puzzle = open(file_name,'r') 

item_0 = 0
item_1 = 0 
list_of_3_sum = [] 
for item in puzzle: 
    list_of_3_sum.append(item_0 + item_1 + int(item))
    item_0 = item_1 
    item_1 = int(item)

print(sum_increased(list_of_3_sum[2:]))