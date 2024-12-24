import numpy as np

# Function to print the Sudoku grid
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

# Function to check if placing num in board[row][col] is valid
def is_valid(board, num, row, col):
    # Check the row
    if num in board[row]:
        return False
    # Check the column
    if num in board[:, col]:
        return False
    # Check the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Function to solve the Sudoku puzzle
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try digits 1-9
                    if is_valid(board, num, row, col):
                        board[row][col] = num  # Place the number
                        if solve_sudoku(board):  # Recursively solve
                            return True
                        board[row][col] = 0  # Backtrack if invalid
                return False  # No valid number found, trigger backtracking
    return True  # Puzzle solved

# Example Sudoku puzzle (0's represent empty cells)
sudoku_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

print("Initial Sudoku Puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Puzzle:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists")
