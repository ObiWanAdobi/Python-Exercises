
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', 'O', '.', '.', '.'],
        ['.', '.', 'O', 'O', '.', '.'],
        ['.', '.', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['.', '.', 'O', 'O', 'O', '.'],
        ['.', '.', 'O', 'O', '.', '.'],
        ['.', '.', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#printing the 2-D list
for j in grid:
    print(j)
print("")

#printing each element of the list
for x in range(9):
    if(x == 4):
        continue
    for y in range(6):
            print(grid[x][y], end='')
    print("")
