file_name = '/Users/ewasu/adventofcode_21/day2/puzzle.txt'
puzzle = open(file_name,'r') 


horizontal = 0 
depth = 0 
for item in puzzle:
    direction, step = item.split(" ")
    if direction == 'forward':
        horizontal = horizontal + int(step)
    if direction == 'down':
        depth = depth + int(step)
    if direction == 'up':
        depth = depth - int(step)

print(horizontal * depth)

file_name = '/Users/ewasu/adventofcode_21/day2/puzzle.txt'
puzzle = open(file_name,'r') 


horizontal = 0 
depth = 0 
aim = 0 
for item in puzzle:
    direction, step = item.split(" ")
    if direction == 'forward':
        horizontal = horizontal + int(step)
        depth = depth + (aim * int(step))
    if direction == 'down':
        aim = aim + int(step)
    if direction == 'up':
        aim = aim - int(step)

print(horizontal * depth)
