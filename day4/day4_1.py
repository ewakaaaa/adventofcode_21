file_name = '/Users/ewasu/adventofcode_21/day4/puzzle.txt'
puzzle = open(file_name,'r') 
lines = puzzle.readlines() 

#print(lines)

numbers = [int(item.replace('\n','')) for item in lines[0].split(",")]

boards = []
board = [] 
for line in lines[2:]: 
    row = [int(item.replace('\n','')) for item in line.split(" ") if item.replace('\n','') != '']
    if len(row) == 0:
        boards.append(board)
        board = [] 
    else: 
        board.append(row)
boards.append(board)


def fun(numbers,boards): 
    for num in numbers: 
        for board in boards: 
            for row in board: 
                if num in row: 
                    row.remove(num)
                    if len(row) == 0: 
                        print("winner!")
                        suma = 0 
                        for row in board: 
                            suma = suma + sum(row)
                        print(suma * num)
                        return(suma * num)

print(fun(numbers,boards))



