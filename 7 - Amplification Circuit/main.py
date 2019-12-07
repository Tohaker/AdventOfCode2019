import csv
import itertools


def read_input():
    with open('input.txt', 'r') as file:
        return [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]


def part_one(input, phase, previous):
    operation_input = [phase, previous]
    input_count = 0

    op_position = 0

    output_list = []

    while input[op_position] != 99:
        opcode = str(input[op_position]).zfill(5)
        instruction = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        # Position mode means we take the value at a position.
        # Immediate mode means we take the value as it is.
        if not params[0]:
            n1 = input[input[op_position + 1]]
        else:
            n1 = input[op_position + 1]

        if not params[1] and instruction != 4 and instruction != 3:
            n2 = input[input[op_position + 2]]
        else:
            n2 = input[op_position + 2]

        location = input[op_position + 3]

        if instruction == 1:
            input[location] = n1 + n2
            op_position += 4
        elif instruction == 2:
            input[location] = n1 * n2
            op_position += 4
        elif instruction == 3:
            n1 = input[op_position + 1]
            input[n1] = operation_input[input_count]
            input_count += 1
            op_position += 2
        elif instruction == 4:
            output_list.append(n1)
            op_position += 2
        elif instruction == 5:
            if n1 != 0:
                op_position = n2
            else:
                op_position += 3
        elif instruction == 6:
            if n1 == 0:
                op_position = n2
            else:
                op_position += 3
        elif instruction == 7:
            if n1 < n2:
                input[location] = 1
            else:
                input[location] = 0
            op_position += 4
        elif instruction == 8:
            if n1 == n2:
                input[location] = 1
            else:
                input[location] = 0
            op_position += 4

    return output_list


def part_two(input, op_position, operation_input):
    input_count = 0

    while input[op_position] != 99:
        opcode = str(input[op_position]).zfill(5)
        instruction = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        # Position mode means we take the value at a position.
        # Immediate mode means we take the value as it is.
        if not params[0]:
            n1 = input[input[op_position + 1]]
        else:
            n1 = input[op_position + 1]

        if not params[1] and instruction != 4 and instruction != 3:
            n2 = input[input[op_position + 2]]
        else:
            n2 = input[op_position + 2]

        if instruction != 4 and instruction != 3:
            location = input[op_position + 3]

        if instruction == 1:
            input[location] = n1 + n2
            op_position += 4
        elif instruction == 2:
            input[location] = n1 * n2
            op_position += 4
        elif instruction == 3:
            n1 = input[op_position + 1]
            input[n1] = operation_input[input_count]
            input_count += 1
            op_position += 2
        elif instruction == 4:
            return n1, op_position + 2, input
        elif instruction == 5:
            if n1 != 0:
                op_position = n2
            else:
                op_position += 3
        elif instruction == 6:
            if n1 == 0:
                op_position = n2
            else:
                op_position += 3
        elif instruction == 7:
            if n1 < n2:
                input[location] = 1
            else:
                input[location] = 0
            op_position += 4
        elif instruction == 8:
            if n1 == n2:
                input[location] = 1
            else:
                input[location] = 0
            op_position += 4

    return 99, 0, input


def run_part_one():
    seqs = itertools.permutations(range(5), 5)
    answers = []

    for seq in seqs:
        input = 0
        for phase in seq:
            input = part_one(read_input(), phase, input)[0]
        answers.append(input)

    return max(answers)


def run_part_two():
    seqs = itertools.permutations(range(5, 10), 5)
    answers = []

    for seq in seqs:
        input = 0
        op_position = [0, 0, 0, 0, 0]
        saved_input = [read_input(), read_input(), read_input(), read_input(), read_input()]
        halt = False
        init = [False, False, False, False, False]
        while not halt:
            for i, phase in enumerate(seq):
                if not init[i]:
                    operation_input = [phase, input]
                    init[i] = True
                else:
                    operation_input = [input]

                result, op_position[i], saved_input[i] = part_two(saved_input[i], op_position[i], operation_input)
                if result == 99:
                    halt = True
                    break
                else:
                    input = result

        answers.append(input)

    return max(answers)


if __name__ == '__main__':
    print(run_part_one())
    print(run_part_two())
