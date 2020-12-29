from intcode import run_computer


def part_one(input):
    program = input[0].split(",")

    return run_computer(program, [1])[1][0]


def part_two(input):
    program = input[0].split(",")

    return run_computer(program, [2])[1][0]