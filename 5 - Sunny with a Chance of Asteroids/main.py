import csv


def read_input():
    with open('input.txt', 'r') as file:
        return [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]


def part_one(input, instruction):
    operation_input = instruction

    op_position = 0

    output_list = []

    while input[op_position] is not 99:
        opcode = str(input[op_position]).zfill(5)
        instruction = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        # Position mode means we take the value at a position.
        # Immediate mode means we take the value as it is.
        if not params[0]:
            n1 = input[input[op_position + 1]]
        else:
            n1 = input[op_position + 1]

        if not params[1] and instruction is not 4 and instruction is not 3:
            n2 = input[input[op_position + 2]]
        else:
            n2 = input[op_position + 2]

        location = input[op_position + 3]

        if instruction is 1:
            input[location] = n1 + n2
            op_position += 4
        elif instruction is 2:
            input[location] = n1 * n2
            op_position += 4
        elif instruction is 3:
            n1 = input[op_position + 1]
            input[n1] = operation_input
            op_position += 2
        elif instruction is 4:
            output_list.append(n1)
            op_position += 2

    return output_list


def part_two(input, instruction):
    operation_input = instruction

    op_position = 0

    output_list = []

    while input[op_position] is not 99:
        opcode = str(input[op_position]).zfill(5)
        instruction = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        # Position mode means we take the value at a position.
        # Immediate mode means we take the value as it is.
        if not params[0]:
            n1 = input[input[op_position + 1]]
        else:
            n1 = input[op_position + 1]

        if not params[1] and instruction is not 4 and instruction is not 3:
            n2 = input[input[op_position + 2]]
        else:
            n2 = input[op_position + 2]

        location = input[op_position + 3]

        if instruction is 1:
            input[location] = n1 + n2
            op_position += 4
        elif instruction is 2:
            input[location] = n1 * n2
            op_position += 4
        elif instruction is 3:
            n1 = input[op_position + 1]
            input[n1] = operation_input
            op_position += 2
        elif instruction is 4:
            output_list.append(n1)
            op_position += 2
        elif instruction is 5:
            if n1 != 0:
                op_position = n2
            else:
                op_position += 3
        elif instruction is 6:
            if n1 == 0:
                op_position = n2
            else:
                op_position += 3
        elif instruction is 7:
            if n1 < n2:
                input[location] = 1
            else:
                input[location] = 0
            op_position += 4
        elif instruction is 8:
            if n1 == n2:
                input[location] = 1
            else:
                input[location] = 0
            op_position += 4

    return output_list

if __name__ == '__main__':
    print(part_one(read_input(), 1))
    print(part_two(read_input(), 5))
