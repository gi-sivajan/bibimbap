# Bibimbap: A Simple Sudoku Solver

This is a simple Python script that can solve Sudoku puzzles using a backtracking algorithm. It's named after what I'm eating while posting this repo. 

## Usage

1. Clone this repository to your local machine:

git clone https://github.com/gi-sivajan/bibimbap.git

2. Open the `bibimbap.py` file and replace the `grid` variable with your Sudoku puzzle. Use `0` to represent empty cells.

3. Run the program:

python bibimbap.py

4. The program will print the solved Sudoku grid if a solution exists. The only error that can be given is one that tells you to check your grid to make sure it is solvable. 
## Example

Here's an example of a Sudoku puzzle represented in the `grid` variable in the `bibimbap.py` file:

```python
grid = [ [5, 3, 0, 0, 7, 0, 0, 0, 0],
 [6, 0, 0, 1, 9, 5, 0, 0, 0],
 [0, 9, 8, 0, 0, 0, 0, 6, 0],
 [8, 0, 0, 0, 6, 0, 0, 0, 3],
 [4, 0, 0, 8, 0, 3, 0, 0, 1],
 [7, 0, 0, 0, 2, 0, 0, 0, 6],
 [0, 6, 0, 0, 0, 0, 2, 8, 0],
 [0, 0, 0, 4, 1, 9, 0, 0, 5],
 [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

## Algorithm

The program uses a backtracking algorithm to solve Sudoku puzzles. It iterates through the grid, attempting to place a number from 1 to 9 in an empty cell while ensuring that it doesn't conflict with the existing numbers in the row, column, or subgrid. If it encounters an invalid move, it backtracks and tries the next number. This process continues until a solution is found or determined to be impossible.

## Future

I may work on adding a better user interface and puzzle generator to the program, but that depends on how quickly I get bored with this altogether. 