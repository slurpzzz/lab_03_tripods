"""
CSAPX Lab 3: Tripods

This module defines the Orientation Enum and the Tripod dataclass,
representing a tripod placement on the grid.

Author: CS RIT
"""

import enum
from dataclasses import dataclass


class Orientation(enum.Enum):
    """
    Represents the four cardinal orientations of a tripod.
    """
    NORTH, EAST, SOUTH, WEST = range(4)


@dataclass
class Tripod:
    """
    Represents a tripod placement on a 2-D grid.
    """
    row: int
    col: int
    orientation: Orientation
    sum: int


def demo() -> None:
    """
    Demonstrate how Orientation enum and Tripod works
    """
    orient = Orientation.NORTH  # orient is NORTH
    if orient == Orientation.NORTH:
        print(orient)  # prints: Orientation.NORTH
        print(orient.name)  # prints: NORTH

    orient = Orientation.SOUTH  # orient is now SOUTH

    # checking if the given string is a valid orientation
    is_valid = "NORTH" in Orientation.__members__
    if is_valid:
        # get the enum constant (Orientation.NORTH) from a string name
        orient = Orientation["NORTH"]

    tripod = Tripod(0,0, Orientation.NORTH, 23)
    print(tripod) # prints: Tripod(row=0, col=0, orientation=<Orientation.NORTH: 0>, sum=23)

if __name__ == '__main__':
    demo()