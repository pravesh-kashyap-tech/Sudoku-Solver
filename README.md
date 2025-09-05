# Sudoku Solver
<br>
🧩 Sudoku Solver (Python)

This project is a console-based Sudoku Solver built in Python using the backtracking algorithm.
It allows users to input their own Sudoku puzzles of any size (4×4, 9×9, 16×16, etc. – as long as the grid size is a perfect square).

🔹 Features

Supports custom grid sizes (N×N where N is a perfect square).

Takes user input for the Sudoku puzzle with 0 representing blank cells.

Uses backtracking to efficiently solve the puzzle.

Displays the Sudoku grid neatly before and after solving.

Handles invalid grid sizes and row input errors gracefully.

Includes a replay option to solve multiple puzzles in one run.

🛠️ How It Works

User enters the Sudoku grid size (e.g., 9 for 9×9 Sudoku).

Inputs the puzzle row by row.

The solver applies the backtracking algorithm:

Places a number only if it follows Sudoku rules (row, column, and subgrid checks).

Recursively solves until the full grid is complete.

The solved Sudoku is displayed in the terminal.
