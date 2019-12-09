import csv


def read_input():
    with open('input.txt', 'r') as file:
        return [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]


def download_more_ram(program, length):
    if len(program) <= length:
        for i in range(len(program), length + 1):
            program.append(0)


def part_one(program, input):
    op_position = 0
    relative_base = 0

    output_list = []

    while program[op_position] != 99:
        opcode = str(program[op_position]).zfill(5)
        instruction = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        # Position mode means we take the value at a position.
        # Immediate mode means we take the value as it is.
        # Relative mode means we take the value at the position of the relative_base.
        if params[0] == 0:
            download_more_ram(program, program[op_position + 1])
            n1 = program[program[op_position + 1]]
        elif params[0] == 1:
            n1 = program[op_position + 1]
        elif params[0] == 2:
            loc = relative_base + program[op_position + 1]
            download_more_ram(program, loc)
            n1 = program[loc]

        if instruction != 3 and instruction != 4 and instruction != 9:
            if params[1] == 0:
                n2 = program[program[op_position + 2]]
            elif params[1] == 1:
                n2 = program[op_position + 2]
            elif params[1] == 2:
                loc = relative_base + program[op_position + 2]
                download_more_ram(program, loc)
                n2 = program[loc]

        if instruction != 3 and instruction != 4 and instruction != 5 and instruction != 9:
            if params[2] == 0 or params[2] == 1:
                location = program[op_position + 3]
                download_more_ram(program, location)
            elif params[2] == 2:
                location = relative_base + program[op_position + 3]
                download_more_ram(program, location)

        if instruction == 1:
            program[location] = n1 + n2
            op_position += 4
        elif instruction == 2:
            program[location] = n1 * n2
            op_position += 4
        elif instruction == 3:
            program[relative_base + program[op_position + 1]] = input
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
                program[location] = 1
            else:
                program[location] = 0
            op_position += 4
        elif instruction == 8:
            if n1 == n2:
                program[location] = 1
            else:
                program[location] = 0
            op_position += 4
        elif instruction == 9:
            relative_base += n1
            op_position += 2

    return output_list


if __name__ == '__main__':
    print(part_one(read_input(), 1))
    print(part_one(read_input(), 2))  # Part Two
