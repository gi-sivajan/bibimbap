def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check if the number is already present in the row or column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check if the number is already present in the subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Undo if it leads to an invalid solution
                return False
    return True

# 0 represents empty cells: 
grid = [
grid = [ [1, 0, 0, 5, 0, 0, 0, 0, 3],
 [0, 3, 7, 0, 0, 1, 0, 0, 4],
 [0, 0, 0, 0, 0, 2, 0, 0, 0],
 [0, 0, 0, 0, 9, 4, 0, 0, 0],
 [0, 0, 4, 0, 0, 0, 0, 3, 2],
 [0, 0, 0, 3, 2, 5, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 2, 0, 0],
 [7, 4, 0, 0, 0, 0, 0, 0, 0],
 [8, 0, 0, 0, 0, 3, 1, 0, 0],
]
]

if solve_sudoku(grid):
    print("Solved puzzle:")
    print_grid(grid)
else:
    print("The provided puzzle is either unsolvable or invalid, please check your grid.")