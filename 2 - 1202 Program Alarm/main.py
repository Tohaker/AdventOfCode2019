import copy


def part_one(input, noun, verb):
    input_copy = copy.copy(input)
    input_copy[1] = noun
    input_copy[2] = verb

    op_position = 0

    while input_copy[op_position] is not 99:
        n1 = input_copy[input[op_position + 1]]
        n2 = input_copy[input[op_position + 2]]
        l = input_copy[op_position + 3]

        if input_copy[op_position] is 1:
            input_copy[l] = n1 + n2
        elif input_copy[op_position] is 2:
            input_copy[l] = n1 * n2

        op_position += 4

    return input_copy


def part_two(input):
    for noun in range(100):
        for verb in range(100):
            i = part_one(input, noun, verb)[0]
            if i == 19690720:
                return noun, verb
    return 0, 0


if __name__ == '__main__':
    input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 6, 19, 23, 2, 23, 6, 27, 1, 5, 27, 31, 1,
             10, 31, 35, 2, 6, 35, 39, 1, 39, 13, 43, 1, 43, 9, 47, 2, 47, 10, 51, 1, 5, 51, 55, 1, 55, 10, 59, 2, 59,
             6, 63, 2, 6, 63, 67, 1, 5, 67, 71, 2, 9, 71, 75, 1, 75, 6, 79, 1, 6, 79, 83, 2, 83, 9, 87, 2, 87, 13, 91,
             1, 10, 91, 95, 1, 95, 13, 99, 2, 13, 99, 103, 1, 103, 10, 107, 2, 107, 10, 111, 1, 111, 9, 115, 1, 115, 2,
             119, 1, 9, 119, 0, 99, 2, 0, 14, 0]
    noun = 12
    verb = 2
    print(part_one(input, noun, verb))

    noun, verb = part_two(input)
    print(100 * noun + verb)
