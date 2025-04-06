def sudoku(puzzle):
    solved = False
    while not solved:
        hasZero = False
        for i in range(0,9):
            for j in range(0,9):
                if puzzle[i][j] == 0:
                    hasZero = True
                    possible = []
                    for digit in range(1,10):
                        if checkRow(puzzle, i, j, digit) & checkCol(puzzle, i, j, digit) & checkBox(puzzle, i, j, digit):
                            possible.append(digit)
                    if len(possible) == 1:
                        puzzle[i][j] = possible[0]
        if not hasZero:
            solved = True
    return puzzle

def checkRow(puzzle, i, j, digit):
    if digit in puzzle[i]:
        return False
    return True

def checkCol(puzzle, i, j, digit):
    for x in range(0, 9):
        if digit == puzzle[x][j]:
            return False
    return True

def checkBox(puzzle, i, j, digit):
    for x in range(0, 3):
        for y in range(0, 3):
            if digit == puzzle[i-(i%3)+x][j-(j%3)+y]:
                return False
    return True