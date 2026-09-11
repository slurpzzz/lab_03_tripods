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

from tripod import *


def read_grid():
    grid = []
    try:
        with open(sys.argv[1], "r") as file:
            file.readline()
            for line in file:
                grid.append([int(x) for x in line.split()])
    except FileNotFoundError, PermissionError, IsADirectoryError, IndexError:
        print("Usage: python3 tripods.py filename")
        sys.exit()
    return grid


def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    if rows <= 50 and cols <= 30:
        for line in grid:
            print(line)
    else:
        print("Too large to print!")
        print(rows, "x", cols)


def get_optimal_orientation(grid, pos):
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
def get_optimal_tripod(grid, pos: tuple[int, int]):
    row, col = pos
    edges = 0
    orientation = Orientation.NORTH
    sum = 0
    if 0 <= row - 1 < len(grid):
        sum += grid[row - 1][col]
    else:
        orientation = Orientation.SOUTH
        edges += 1
    if 0 <= col + 1 < len(grid[0]):
        sum += grid[row][col + 1]
    else:
        orientation = Orientation.WEST
        edges += 1
    if 0 <= row + 1 < len(grid):
        sum += grid[row + 1][col]
    else:
        orientation = Orientation.NORTH
        edges += 1
    if 0 <= col - 1 < len(grid[0]):
        sum += grid[row][col - 1]
    else:
        orientation = Orientation.EAST
        edges += 1
    if edges >= 2:
        return None
    if edges == 1:
        return Tripod(row, col, orientation, sum)
    orientation = get_optimal_orientation(grid, pos)
    if orientation == Orientation.NORTH:
        sum -= grid[row + 1][col]
    elif orientation == Orientation.EAST:
        sum -= grid[row][col - 1]
    elif orientation == Orientation.SOUTH:
        sum -= grid[row - 1][col]
    else:
        sum -= grid[row][col + 1]
    return Tripod(row, col, orientation, sum)


def compute_tripod_locations(grid):
    tripods = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            tripod = get_optimal_tripod(grid, (i, j))
            if tripod:
                tripods.append(tripod)

    return tripods


def insertion_sort(data: list[Tripod]):
    if len(data) <= 1:
        return
    for i in range(1, len(data)):
        j = i-1
        while data[i].sum < data[j].sum and j>=0 and i>=0:
            data[i], data[j] = data[j], data[i]
            i-=1
            j-=1


def hybrid_sort(data, k):
    if len(data) <= k:
        insertion_sort(data)


def main() -> None:
    grid = read_grid()
    print(f"Rows: {len(grid)} Columns: {len(grid[0])}")
    print_grid(grid)
    num_tripods = int(input("How many tripods to place? "))
    if num_tripods > len(grid) * len(grid[0]) - 4:
        print("Too many tripods!")
    locs = compute_tripod_locations(grid)
    insertion_sort(locs)
    for tripod in locs:
        print(f"({tripod.row}, {tripod.col}) {tripod.orientation} {tripod.sum}")


if __name__ == "__main__":
    main()
