import statistics

for i in range(0,13):
    bit = [] 
    file_name = '/Users/ewasu/adventofcode_21/day3/puzzle.txt'
    puzzle = open(file_name,'r') 
    lines = puzzle.readlines() 

    if len(lines) == 1: 
        oxygen_generator_rating = int(lines[0], 2)
        print(oxygen_generator_rating)
        break

    for line in lines:
        bit.append(int(line[i]))
        most_common = max(statistics.multimode(bit)) 
        #most_common = int(not bool(most_common))
    
    puzzle.close()
    puzzle = open(file_name,'w') 
    
    for line in lines: 
        if int(line[i]) == most_common:
            puzzle.write(line)
    puzzle.close()

