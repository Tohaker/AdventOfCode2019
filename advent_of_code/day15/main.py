from intcode import run_computer
from enum import Enum
import matplotlib.pyplot as plt


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Status(Enum):
    WALL = 0
    MOVED = 1
    OXYGEN = 2


def next_position(coord, dir):
    if dir == Direction.NORTH:
        return (coord[0], coord[1] - 1)
    elif dir == Direction.SOUTH:
        return (coord[0], coord[1] + 1)
    elif dir == Direction.WEST:
        return (coord[0] - 1, coord[1])
    elif dir == Direction.EAST:
        return (coord[0] + 1, coord[1])


def next_direction(dir):
    if dir == Direction.NORTH:
        return Direction.EAST
    elif dir == Direction.SOUTH:
        return Direction.WEST
    elif dir == Direction.WEST:
        return Direction.NORTH
    elif dir == Direction.EAST:
        return Direction.SOUTH


def find_undiscovered_directions(coord, grid):
    direction = Direction.NORTH
    tiles = []
    for _ in range(4):
        if next_position(coord, direction) not in grid:
            tiles.append(direction)

        direction = next_direction(direction)

    return tiles


def find_adjacent_empty_tiles(coord, grid):
    direction = Direction.NORTH
    tiles = []
    for _ in range(4):
        c = next_position(coord, direction)
        if c in grid and grid[c] == ".":
            tiles.append(direction)

        direction = next_direction(direction)

    return tiles


def part_one(input):
    program = input[0].split(",")

    op_position = 0
    relative_base = 0

    grid = {(0, 0): "."}
    direction = Direction.NORTH
    position = (0, 0)

    while True:
        program, outputs, op_position, relative_base = run_computer(
            program, [direction.value], op_position, relative_base, feedback=True
        )

        status = Status(outputs[0])

        if status == Status.OXYGEN:
            break
        elif status == Status.MOVED:
            position = next_position(position, direction)
            grid[position] = "."
        elif status == Status.WALL:
            grid[next_position(position, direction)] = "#"
            undiscovered = find_undiscovered_directions(position, grid)

            if len(undiscovered) > 0:
                direction = undiscovered[0]
            else:
                direction = find_adjacent_empty_tiles(position, grid)[0]

    x = [k[0] for k, v in grid.items() if v == "."]
    y = [k[1] for k, v in grid.items() if v == "."]

    plt.scatter(x, y)
    plt.savefig("day15_part1.png")


def part_two(input):
    program = input[0].split(",")
