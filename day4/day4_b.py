import numpy as np

# read puzzle
file_name = "/Users/ewasu/adventofcode_21/day4/puzzle.txt"
puzzle = open(file_name, "r")
lines = puzzle.readlines()
numbers = [int(item.replace("\n", "")) for item in lines[0].split(",")]

boards = []
board = []
for line in lines[2:]:
    row = [
        int(item.replace("\n", ""))
        for item in line.split(" ")
        if item.replace("\n", "") != ""
    ]
    if len(row) == 0:
        boards.append(np.array(board))
        board = []
    else:
        board.append(row)
boards.append(np.array(board))

# solution
boards_left = [i for i in range(0, len(boards))]

for num in numbers:
    for board_num, board in enumerate(boards):
        for row in range(0, board.shape[0]):
            for col in range(0, board.shape[1]):
                if board[row][col] == num:
                    board[row][col] = -1
        for i in range(0, board.shape[0]):
            if (board[i] == [-1, -1, -1, -1, -1]).all() or (
                board[:, i] == [-1, -1, -1, -1, -1]
            ).all():
                if board_num in boards_left:
                    boards_left.remove(board_num)
                    print("winner!")
                    board[board == -1] = 0
                    print(board.sum() * num)
