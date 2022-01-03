import statistics

gamma = []
i = 0
for i in range(0, 5):
    bit = []
    file_name = "/Users/ewasu/adventofcode_21/day3/puzzle.txt"
    puzzle = open(file_name, "r")
    for item in puzzle:
        bit.append(int(item[i]))
    gamma.append(statistics.mode(bit))

# revert
epsilon = [str(int(not bool(item))) for item in gamma]

# int -> str and bit -> int
gamma = int("".join([str(i) for i in gamma]), 2)
epsilon = int("".join(epsilon), 2)

print(epsilon * gamma)
