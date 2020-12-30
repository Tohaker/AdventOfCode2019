from intcode import run_computer
from itertools import groupby


def check_if_destroyed_blocks(grid, coordinates, joystick, paddle):
    if grid[coordinates] == 4:
        if coordinates[0] < paddle[0]:
            joystick = -1
        elif coordinates[0] > paddle[0]:
            joystick = 1
        else:
            joystick = 0

    return joystick


def part_one(input):
    program = input[0].split(",")

    op_position = 0
    relative_base = 0

    grid = {}

    while True:
        program, outputs, op_position, relative_base = run_computer(
            program,
            initial_position=op_position,
            initial_relative_base=relative_base,
            feedback=True,
            feedback_threshold=3,
        )

        if len(outputs) == 0:
            break

        coordinates = (outputs[0], outputs[1])
        grid[coordinates] = outputs[2]

    return [(k, len(list(v))) for k, v in groupby(sorted(grid.values()))][2][1]


def part_two(input):
    program = input[0].split(",")
    program[0] = 2

    op_position = 0
    relative_base = 0
    joystick = 0

    score = 0

    grid = {}
    empty = []
    walls = []
    blocks = []
    paddle = (0, 0)

    while True:
        program, outputs, op_position, relative_base = run_computer(
            program,
            input=[joystick],
            initial_position=op_position,
            initial_relative_base=relative_base,
            feedback=True,
            feedback_threshold=3,
        )

        if len(outputs) == 0:
            break

        coordinates = (outputs[0], outputs[1])

        if coordinates == (-1, 0):
            score = outputs[2]
        else:
            grid[coordinates] = outputs[2]

            # Plotting the game
            value = grid[coordinates]
            if value == 0:
                empty.append(coordinates)
            elif value == 1:
                walls.append(coordinates)
            elif value == 2:
                blocks.append(coordinates)
            elif value == 3:
                paddle = coordinates

            joystick = check_if_destroyed_blocks(grid, coordinates, joystick, paddle)

    return score