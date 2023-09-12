def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check if the number is already present in the row or column
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check if the number is already present in the subgrid
    subgrid_size = int(len(grid) ** 0.5)
    start_row, start_col = subgrid_size * (row // subgrid_size), subgrid_size * (col // subgrid_size)
    for i in range(start_row, start_row + subgrid_size):
        for j in range(start_col, start_col + subgrid_size):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 0:
                for num in range(1, len(grid) + 1):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Undo if it leads to an invalid solution
                return False
    return True

def create_empty_grid(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def input_grid_values(grid_size):
    grid = []

    print(f"Enter the {grid_size}x{grid_size} Sudoku grid values row by row, using 0 to represent empty cells.")
    for _ in range(grid_size):
        while True:
            row_input = input(f"Enter row ({grid_size} values separated by spaces): ")
            row_values = row_input.split()
            if len(row_values) == grid_size:
                try:
                    grid.append([int(val) for val in row_values])
                    break
                except ValueError:
                    print(f"Please enter {grid_size} numbers.")
            else:
                print(f"Please enter {grid_size} values separated by spaces.")

    return grid

# Determine the size of the puzzle grid 
while True:
    grid_size = input("Enter the size of the Sudoku grid (9 or 16): ")
    if grid_size in ["9", "16"]:
        break
    else:
        print("Please enter 9 or 16. Support for larger grids may come in the future!")

grid_size = int(grid_size)
grid = input_grid_values(grid_size)

if solve_sudoku(grid):
    print("\nSolved puzzle:")
    print_grid(grid)
else:
    print("\nThe provided puzzle is either unsolvable or invalid, please check your grid.")
