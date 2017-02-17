from itertools import permutations as perm
from time import sleep

def checkColumn(s):
    columns = [[s[i][j] for i in range(4)] for j in range(4)]
    values = [1 if len(set(col))==4 else 0 for col in columns]
    if sum(values)==4:
        return True
    return False

def checkSquares(s):
    values = 0
    if len(set([s[i][j] for i in range(0,2) for j in range(0,2)]))!=4:
        return False
    if len(set([s[i][j] for i in range(0,2) for j in range(2,4)]))!=4:
        return False
    if len(set([s[i][j] for i in range(2,4) for j in range(0,2)]))!=4:
        return False
    if len(set([s[i][j] for i in range(2,4) for j in range(2,4)]))!=4:
        return False
    return True

def checkSol(s):
    if not checkColumn(s):
        return False
    if checkSquares(s):
        return True
    return False

def sudoku():
    base_perm = perm([1, 2, 3, 4], 4)
    sol = perm(base_perm, 4)
    for s in sol:
        if checkSol(s):
            yield list(s)
