#!/usr/bin/python3
"""Module to solve the Nqueens problem"""
import sys


def generate_solutions(row, column):
    """Generate solutions for the N Queens problem up to a given row.

    Args:
        row (int): The current row being processed.
        column (int): The size of the chessboard.

    Returns:
        list: A list of valid queen placements.
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution

def place_queen(queen, column, prev_solution):
    """Place a queen on the chessboard while maintaining valid placements.

    Args:
        queen (int): The current queen's row.
        column (int): The size of the chessboard.
        prev_solution (list): Previous valid queen placements.

    Returns:
        list: Valid placements for the current row.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position

def is_safe(q, x, array):
    """Check if placing a queen at a given position is safe.

    Args:
        q (int): The current queen's row.
        x (int): The column to be checked for queen placement.
        array (list): List of previous queen placements.

    Returns:
        bool: True if placing the queen is safe, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))

def init():
    """Initialize the N value and perform input validation.

    Returns:
        int: The validated N value.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def n_queens():
    """Solve and print solutions for the N Queens problem."""
    n = init()
    solutions = generate_solutions(n, n)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

if __name__ == '__main__':
    n_queens()
