"""
CSAPX Lab 3: Tripods

A program that finds the optimal placement of a number of tripods in a grid
of numbers.  A tripod can touch three adjacent cells, based on orientation,
e.g. a north facing tripod touches the east, south and west cells.

The goal is to find the placement of a number of tripods, such that the
total sums of the cells that all combined tripods touch is maximum.

Usage: python3 tripods.py filename

author: Justin Spadone
"""

import sys

from tripod import Tripod, Orientation
from hybrid_sort import hybrid_sort


def read_grid() -> list[list[int]]:
    """
    Reads the 2nd command line argument as a file and parses it into a list of integers
    :return: The 2D list of integers representing the grid
    """
    grid = []
    try:
        with open(sys.argv[1], "r") as file:
            file.readline()
            for line in file:
                grid.append([int(x) for x in line.split()])
    except (FileNotFoundError, PermissionError, IsADirectoryError, IndexError):
        print("Usage: python3 tripods.py filename")
        sys.exit()
    return grid


def print_grid(grid: list[list[int]]) -> None:
    """
    Prints the grid if it is small enough, otherwise prints that it is too large
    :param grid: The 2D list of integers to print
    :return: None
    """
    rows = len(grid)
    cols = len(grid[0])
    print(f"Rows: {rows} Columns: {cols}")
    if rows <= 50 and cols <= 30:
        for row in grid:
            for cell in row:
                print(cell, end=' ')
            print()
    else:
        print("Too large to print!")


def get_optimal_orientation(grid: list[list[int]], pos: tuple[int, int]):
    """

    :param grid:
    :param pos:
    :return:
    """
    row, col = pos
    neighbors = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
    min_val = grid[neighbors[0][0]][neighbors[0][1]]
    min_index = 0
    for index, neighbor in enumerate(neighbors):
        if grid[neighbor[0]][neighbor[1]] < min_val:
            min_val = grid[neighbor[0]][neighbor[1]]
            min_index = index
    orientation = Orientation.NORTH
    if min_index == 0:
        orientation = Orientation.SOUTH
    elif min_index == 1:
        orientation = Orientation.WEST
    elif min_index == 2:
        orientation = Orientation.NORTH
    else:
        orientation = Orientation.EAST
    return orientation


# if N,S,E,W is out of bounds, orientation is facing the other direction
def get_optimal_tripod(grid: list[list[int]], pos: tuple[int, int]):
    row, col = pos
    edges = 0
    orientation = Orientation.NORTH
    total = 0
    if 0 <= row - 1 < len(grid):
        total += grid[row - 1][col]
    else:
        orientation = Orientation.SOUTH
        edges += 1
    if 0 <= col + 1 < len(grid[0]):
        total += grid[row][col + 1]
    else:
        orientation = Orientation.WEST
        edges += 1
    if 0 <= row + 1 < len(grid):
        total += grid[row + 1][col]
    else:
        orientation = Orientation.NORTH
        edges += 1
    if 0 <= col - 1 < len(grid[0]):
        total += grid[row][col - 1]
    else:
        orientation = Orientation.EAST
        edges += 1
    if edges >= 2:
        return None
    if edges == 1:
        return Tripod(row, col, orientation, total)
    orientation = get_optimal_orientation(grid, pos)
    if orientation == Orientation.NORTH:
        total -= grid[row + 1][col]
    elif orientation == Orientation.EAST:
        total -= grid[row][col - 1]
    elif orientation == Orientation.SOUTH:
        total -= grid[row - 1][col]
    else:
        total -= grid[row][col + 1]
    return Tripod(row, col, orientation, total)


def compute_tripod_locations(grid: list[list[int]]):
    tripods = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            tripod = get_optimal_tripod(grid, (i, j))
            if tripod:
                tripods.append(tripod)

    return tripods


def main() -> None:
    grid = read_grid()
    print_grid(grid)
    num_tripods = int(input("Number of tripods: "))
    max_tripods = len(grid) * len(grid[0]) - 4
    if num_tripods > max_tripods:
        print("Too many tripods!")
        sys.exit()

    tripods = compute_tripod_locations(grid)
    tripods = hybrid_sort(tripods, 32)
    tripods = tripods[-1:-num_tripods - 1:-1]
    print('Optimal placement:')
    for tripod in tripods:
        print(f"location: ({tripod.row},{tripod.col}), orientation: {tripod.orientation.name}, sum: {tripod.sum}")
    total = sum(tripod.sum for tripod in tripods)
    print('Total sum:', total)


if __name__ == "__main__":
    main()
