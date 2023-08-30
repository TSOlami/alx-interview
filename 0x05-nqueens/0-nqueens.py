#!/usr/bin/python3
"""Module to solve the Nqueens problem"""
import sys

def place_queens(row, n):
    """Generate valid placements for the queens on the chessboard.

    Args:
        row (int): The current row to consider placing a queen.
        n (int): The size of the chessboard.

    Returns:
        list: List of valid placements for queens up to the current row.
    """
    # Base case: All rows have been processed, return an empty placement.
    if row == n:
        return [[]]

    valid_placements = []
    # Generate valid placements for the next row.
    prev_placements = place_queens(row + 1, n)

    # Iterate through columns to find valid positions for the queen in the current row.
    for prev_placement in prev_placements:
        for col in range(n):
            # Check if placing a queen at (row, col) is safe.
            if is_safe(row, col, prev_placement):
                valid_placements.append(prev_placement + [col])

    return valid_placements

def is_safe(row, col, placement):
    """Check if placing a queen at (row, col) is safe.

    Args:
        row (int): The row of the queen to be placed.
        col (int): The column of the queen to be placed.
        placement (list): List of previous placements of queens.

    Returns:
        bool: True if placing the queen is safe, False otherwise.
    """
    for prev_row, prev_col in enumerate(placement):
        # Check if there's a queen in the same column or diagonally attacking.
        if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
            return False
    return True

def solve_nqueens():
    """Solve the N Queens problem and display solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    
    n = int(sys.argv[1])
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = place_queens(0, n)
    
    # Display solutions with pairs (row, col) of queen placements.
    for solution in solutions:
        solution_pairs = [[row, col] for row, col in enumerate(solution)]
        print(solution_pairs)

if __name__ == '__main__':
    solve_nqueens()
