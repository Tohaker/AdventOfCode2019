from copy import copy
from itertools import permutations
from intcode import run_computer


def run_sequence(program, sequence):
    next_input = 0
    for phase in sequence:
        next_input = run_computer(copy(program), [phase, next_input])[1][0]

    return next_input


def run_feedback(program, sequence):
    next_input = 0
    previous_command = 0
    saved_position = [0] * len(sequence)
    saved_state = list(map(lambda s: copy(program), sequence))

    for i, phase in enumerate(sequence):
        saved_state[i], outputs, saved_position[i], _ = run_computer(
            saved_state[i], [phase, next_input], saved_position[i], feedback=True
        )
        next_input = outputs[0]

    while previous_command != 99:
        for i, _ in enumerate(sequence):
            saved_state[i], outputs, saved_position[i], _ = run_computer(
                saved_state[i], [next_input], saved_position[i], feedback=True
            )
            previous_command = saved_state[i][saved_position[i]]

            if len(outputs) == 0:
                break

            next_input = outputs[0]

    return next_input


def part_one(input):
    program = input[0].split(",")

    return max(
        map(lambda sequence: run_sequence(program, sequence), list(permutations([0, 1, 2, 3, 4])))
    )


def part_two(input):
    program = input[0].split(",")

    return max(
        map(lambda sequence: run_feedback(program, sequence), list(permutations([5, 6, 7, 8, 9])))
    )
