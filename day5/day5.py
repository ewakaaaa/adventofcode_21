import numpy as np 

file_name = '/Users/ewasu/adventofcode_21/day5/puzzle.txt'
puzzle = open(file_name,'r') 
lines = puzzle.readlines() 

x = []
y = [] 

for line in lines:
    start, end = line.split(" -> ")
    x1,y1 = start.split (",")
    x2,y2 = end.split (",")
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)

t = np.zeros(shape=(max(x1,x2)+1,max(y1,y2)+1))

for line in lines:
    start, end = line.split(" -> ")
    x1,y1 = start.split (",")
    x2,y2 = end.split (",")
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    x_min = min(x1,x2)
    x_max = max(x1,x2)
    y_min = min(y1,y2)
    y_max = max(y1,y2)

    if x1 == x2: 
        for i in range(y_min,y_max+1,1):
            t[x1][i] = t[x2][i] + 1 
    
    else: 
        A = np.array([[x1, 1], [x2, 1]])
        inv_A = np.linalg.inv(A)
        B = np.array([y1, y2])
        X = np.linalg.inv(A).dot(B)
        tanges = round(X[0],0)

        if tanges == -1:
            for i ,j in zip(range(x_min,x_max+1,1), range(y_max,y_min-1,-1)):
                t[i][j] = t[i][j] + 1 
        if tanges == 1: 
            for i ,j in zip(range(x_min,x_max+1,1), range(y_min,y_max+1,1)):
                t[i][j] = t[i][j] + 1 
        if tanges == 0:
            for i in range(x_min,x_max+1,1):
                t[i][y1] = t[i][y1] + 1 

t[t < 2] = 0
t[t >= 2 ] = 1 
print(t.sum())
