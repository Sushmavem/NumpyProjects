# Sudoku Solver with Tkinter

This project implements a Sudoku solver using backtracking and provides a graphical user interface (GUI) to solve Sudoku puzzles. The user can input their puzzle into the grid and click the "Solve" button to find the solution.

## Requirements

- Python 3.x
- tkinter (comes pre-installed with Python)

No additional libraries are needed as tkinter is part of the standard Python library.

## Project Overview

This script uses the following key features:

1. **Backtracking Algorithm**: The puzzle is solved using a backtracking approach, where the program fills in numbers, checks if they are valid according to Sudoku rules, and backtracks when a conflict is found.
2. **Graphical User Interface (GUI)**: The GUI is created using the Tkinter library, allowing the user to input the puzzle and visualize the solution.
3. **Sudoku Rules**: The solution ensures that each row, column, and 3x3 subgrid contains all digits from 1 to 9 with no repetition.

## How to Run

1. Clone or download this repository to your local machine.
2. Run the script using:

```bash
python sudoku_solver.py

3. A window will appear with a 9x9 grid where you can enter the Sudoku puzzle.
4. Click the "Solve" button to find the solution, or see the message if no solution exists.

Example GUI

## Functions
is_valid(board, row, col, num): Checks if placing a number at a specific location is valid according to Sudoku rules (no duplicates in row, column, or subgrid).
solve_sudoku(board): Solves the Sudoku puzzle using the backtracking algorithm.
find_empty_location(board): Finds an empty location (represented by 0) in the Sudoku grid.
update_gui_board(board, entry_widgets): Updates the GUI grid to reflect the solved Sudoku board.
solve_button_click(board, entry_widgets): Handles the click event for the "Solve" button, converts the GUI input into a board, solves the puzzle, and updates the GUI.
create_sudoku_gui(): Initializes the GUI and starts the Tkinter event loop.

## Example Output
Input your puzzle into the GUI grid.
Click the Solve button.
The puzzle will be solved and the solution displayed in the grid.