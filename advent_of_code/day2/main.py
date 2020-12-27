from intcode import run_computer


def part_one(input):
    # Downloaded input is on one line
    input = input[0].split(',')

    input[1] = '12'
    input[2] = '2'

    result = run_computer(input)
    return result[0][0]


def part_two(input):
    # Downloaded input is on one line
    input = input[0].split(',')

    for i in range(0, 100):
        for j in range(0, 100):
            input[1] = str(i)
            input[2] = str(j)
            if run_computer(input)[0][0] == 19690720:
                return 100 * i + j
