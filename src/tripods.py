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


def read_grid():
    grid = []
    try:
        with open(sys.argv[1], "r") as file:
            line_0 = file.readline().split()
            rows, cols = [int(x) for x in line_0]
            print(rows, cols)
            for line in file:
                grid.append([int(x) for x in line.split()])
    except FileNotFoundError, PermissionError, IsADirectoryError:
        print("Usage: python3 tripods.py filename")
    return grid


def print_grid(grid):
    if len(grid) <= 50 and len(grid[0]) <= 30:
        for line in grid:
            print(line)
    else:
        print("Too large to print!")


def main() -> None:
    # print(sys.argv)
    grid = read_grid()

    num_tripods = int(input("How many tripods to place? "))
    if num_tripods > len(grid) * len(grid[0]) - 4:
        print("Too many tripods!")


if __name__ == "__main__":
    main()
