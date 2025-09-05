import os
import math

def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def print_grid(grid, n):
    """Print Sudoku grid neatly"""
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()

def is_safe(grid, row, col, num, n, subgrid_size):
    """Check if placing a number is valid"""
    # Row check
    for x in range(n):
        if grid[row][x] == num:
            return False

    # Column check
    for x in range(n):
        if grid[x][col] == num:
            return False

    # Subgrid check
    start_row = row - row % subgrid_size
    start_col = col - col % subgrid_size
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(grid, row, col, n, subgrid_size):
    """Backtracking Sudoku solver"""
    if row == n - 1 and col == n:
        return True
    if col == n:
        row += 1
        col = 0
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1, n, subgrid_size)

    for num in range(1, n + 1):
        if is_safe(grid, row, col, num, n, subgrid_size):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1, n, subgrid_size):
                return True
        grid[row][col] = 0

    return False


def play_game():
    clear_screen()
    print("🎮 Sudoku Solver Game")
    n = int(input("Enter grid size (must be a perfect square, e.g., 4, 9, 16): "))

    # Check if grid size is valid
    subgrid_size = int(math.sqrt(n))
    if subgrid_size * subgrid_size != n:
        print("⚠️ Invalid grid size! It must be a perfect square (e.g., 4, 9, 16).")
        return

    print(f"\nEnter your Sudoku grid ({n} rows, {n} numbers per row, use 0 for blanks):")
    sudoku_grid = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print(f"⚠️ Each row must have exactly {n} numbers!")
            return
        sudoku_grid.append(row)

    print("\nYour Input Sudoku:")
    print_grid(sudoku_grid, n)

    if solve_sudoku(sudoku_grid, 0, 0, n, subgrid_size):
        print("\n✅ Solved Sudoku:")
        print_grid(sudoku_grid, n)
    else:
        print("\n❌ No solution exists!")


if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nDo you want to solve another Sudoku? (y/n): ").strip().lower()
        if again != "y":
            clear_screen()
            print("👋 Thanks for playing!")
            break
