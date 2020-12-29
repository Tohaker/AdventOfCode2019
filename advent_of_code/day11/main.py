from intcode import run_computer
from enum import Enum, auto
import matplotlib.pyplot as plt


class Direction(Enum):
    FORWARD = auto()
    BACKWARD = auto()
    LEFT = auto()
    RIGHT = auto()


def state_machine(current, new):
    state = {
        Direction.FORWARD: {0: Direction.LEFT, 1: Direction.RIGHT},
        Direction.BACKWARD: {0: Direction.RIGHT, 1: Direction.LEFT},
        Direction.LEFT: {0: Direction.BACKWARD, 1: Direction.FORWARD},
        Direction.RIGHT: {0: Direction.FORWARD, 1: Direction.BACKWARD},
    }

    return state.get(current).get(new)


def move_robot(direction, current_panel):
    if direction == Direction.FORWARD:
        return current_panel[0], current_panel[1] + 1
    elif direction == Direction.BACKWARD:
        return current_panel[0], current_panel[1] - 1
    elif direction == Direction.LEFT:
        return current_panel[0] - 1, current_panel[1]
    elif direction == Direction.RIGHT:
        return current_panel[0] + 1, current_panel[1]


def map_panel(program, starting_colour):
    panel = {(0, 0): starting_colour}
    current_panel = (0, 0)
    current_direction = Direction.FORWARD
    op_position = 0
    relative_base = 0

    while True:
        input = [panel[current_panel]] if current_panel in panel else [0]

        program, outputs, op_position, relative_base = run_computer(
            program, input, op_position, relative_base, feedback=True, feedback_threshold=2
        )

        if len(outputs) == 0:
            break

        # Paint the current panel
        panel[current_panel] = outputs[0]

        # Figure out which way to turn
        current_direction = state_machine(current_direction, outputs[1])
        current_panel = move_robot(current_direction, current_panel)

    return panel


def part_one(input):
    program = input[0].split(",")
    panel = map_panel(program, 0)

    return len(panel)


def part_two(input):
    program = input[0].split(",")
    panel = map_panel(program, 1)

    x = [coord[0] for coord, value in panel.items() if value == 1]
    y = [coord[1] for coord, value in panel.items() if value == 1]

    plt.scatter(x, y)
    plt.savefig("day11_part2.png")

    return 0
