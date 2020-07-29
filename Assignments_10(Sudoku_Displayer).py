sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
new_sudoku = []
for i in range(len(sudoku)):
    new_sudoku.append(sudoku[i][0:3] + ["|"] + sudoku[i][3:6] + ["|"] + sudoku[i][6:])
    if i % 4 == 0:
        new_sudoku.insert(i, 11*"-")
new_sudoku.append(11*"-")

for i in range(len(new_sudoku)):
    print(*new_sudoku[i])
