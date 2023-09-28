#!/usr/bin/python3
"""Solving the Island perimeter problem
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Check grid dimensions
    assert 1 <= rows <= 100, "Number of rows must be between 1 and 100"
    assert 1 <= cols <= 100, "Number of columns must be between 1 and 100"

    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]

            # Check if the cell is either land or water
            assert cell in (0, 1), "Grid values must be 0 or 1"

            if cell == 1:
                perimeter += 4  # Start with 4 sides for the land cell

                # Check adjacent cells (up, down, left, and right)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1  # Subtract 1 for the shared side
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
