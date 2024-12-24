import tkinter as tk
from tkinter import messagebox


# Function to check if the board is valid (rows, columns, and 3x3 grid should not have duplicates)
def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# Function to solve the puzzle using backtracking
def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Undo the choice (backtrack)

    return False  # Trigger backtracking


# Function to find an empty location in the board
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


# Function to update the Sudoku board in the GUI
def update_gui_board(board, entry_widgets):
    for i in range(9):
        for j in range(9):
            value = board[i][j]
            entry_widgets[i][j].delete(0, tk.END)
            if value != 0:
                entry_widgets[i][j].insert(tk.END, str(value))


# Function to handle the solve button click
def solve_button_click(board, entry_widgets):
    # Convert the GUI entries to a 2D list (board)
    for i in range(9):
        for j in range(9):
            try:
                board[i][j] = int(entry_widgets[i][j].get())
            except ValueError:
                pass  # Ignore invalid input, keep as 0

    if solve_sudoku(board):
        update_gui_board(board, entry_widgets)
    else:
        messagebox.showinfo("Solution", "No solution exists!")


# Function to create the Sudoku board GUI
def create_sudoku_gui():
    # Initialize a 9x9 board with zeros (empty)
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Create the main window
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("500x500")
    root.config(bg='blue')  # Set the background color of the window to blue

    # Create a grid of entry widgets (9x9)
    entry_widgets = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            entry_widgets[i][j] = tk.Entry(root, width=3, font=("Helvetica", 18), justify="center", bd=2)
            entry_widgets[i][j].grid(row=i, column=j, padx=5, pady=5)
            entry_widgets[i][j].config(bg="#d3d3d3")  # Light grey background for entry cells

    # Solve button with a nice color and functionality
    solve_button = tk.Button(root, text="Solve", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=lambda: solve_button_click(board, entry_widgets))
    solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    # Start the Tkinter event loop
    root.mainloop()


# Run the application
create_sudoku_gui()
