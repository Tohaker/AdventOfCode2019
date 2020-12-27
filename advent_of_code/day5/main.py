from intcode import run_computer


def part_one(input):
    # Downloaded input is on one line
    program = input[0].split(',')

    return list(filter(bool, run_computer(program, 1)[1]))[0]


def part_two(input):
    # Downloaded input is on one line
    program = input[0].split(',')

    return list(filter(bool, run_computer(program, 5)[1]))[0]
