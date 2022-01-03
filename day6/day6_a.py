file_name = "/Users/ewasu/adventofcode_21/day6/puzzle.txt"
puzzle = open(file_name, "r")
lines = puzzle.readlines()

fish = [int(item) for item in lines[0].split(",")]

day = 0
while day != 256:
    for i, fish_clock in enumerate(fish):
        if fish_clock == 0:
            fish[i] = 6
            fish.append(9)
        else:
            fish[i] = fish_clock - 1
    day = day + 1

print(len(fish))
