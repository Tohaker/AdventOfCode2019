from enum import Enum


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def get_value(program, position, mode):
    next_val = program[position]

    if Mode(mode) is Mode.POSITION:
        return program[next_val]
    elif Mode(mode) is Mode.IMMEDIATE:
        return next_val


def run_computer(program, input=0):
    position = 0
    outputs = []
    program = list(map(int, program))

    while program[position] != 99:
        opcode = str(program[position]).zfill(5)
        command = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        if command == 1:
            n1 = get_value(program, position + 1, params[0])
            n2 = get_value(program, position + 2, params[1])

            # Location to write to will always be the immediate value
            location = get_value(program, position + 3, Mode.IMMEDIATE)

            program[location] = n1 + n2
            position += 4

        elif command == 2:
            n1 = get_value(program, position + 1, params[0])
            n2 = get_value(program, position + 2, params[1])

            # Location to write to will always be the immediate value
            location = get_value(program, position + 3, Mode.IMMEDIATE)

            program[location] = n1 * n2
            position += 4

        elif command == 3:
            # Location to write to will always be the immediate value
            location = get_value(program, position + 1, Mode.IMMEDIATE)

            program[location] = input
            position += 2

        elif command == 4:
            value = get_value(program, position + 1, params[0])
            outputs.append(value)
            position += 2

        elif command == 5:
            to_check = get_value(program, position + 1, params[0])
            new_position = get_value(program, position + 2, params[1])

            if (to_check != 0):
                position = new_position
            else:
                position += 3

        elif command == 6:
            to_check = get_value(program, position + 1, params[0])
            new_position = get_value(program, position + 2, params[1])

            if (to_check == 0):
                position = new_position
            else:
                position += 3

        elif command == 7:
            p1 = get_value(program, position + 1, params[0])
            p2 = get_value(program, position + 2, params[1])

            # Location to write to will always be the immediate value
            location = get_value(program, position + 3, Mode.IMMEDIATE)

            if (p1 < p2):
                program[location] = 1
            else:
                program[location] = 0

            position += 4

        elif command == 8:
            p1 = get_value(program, position + 1, params[0])
            p2 = get_value(program, position + 2, params[1])

            # Location to write to will always be the immediate value
            location = get_value(program, position + 3, Mode.IMMEDIATE)

            if (p1 == p2):
                program[location] = 1
            else:
                program[location] = 0

            position += 4

    return program, outputs
