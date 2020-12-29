from enum import Enum


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def get_value(program, position, relative_base, mode):
    if position >= len(program):
        next_val = 0
    else:
        next_val = program[position]

    if Mode(mode) is Mode.POSITION:
        return get_value(program, next_val, relative_base, Mode.IMMEDIATE)
    elif Mode(mode) is Mode.IMMEDIATE:
        return next_val
    elif Mode(mode) is Mode.RELATIVE:
        return program[relative_base + next_val] if relative_base + next_val < len(program) else 0


def write_value(program, location, value):
    if location >= len(program):
        program = program + [0] * (location - len(program) + 1)

    program[location] = value

    return program


def run_computer(
    program,
    input=[0],
    initial_position=0,
    feedback=False,
):
    position = initial_position
    relative_base = 0
    input_counter = 0
    outputs = []
    program = list(map(int, program))

    while program[position] != 99:
        opcode = str(program[position]).zfill(5)
        command = int(opcode[-2:])
        params = [int(opcode[2:3]), int(opcode[1:2]), int(opcode[:1])]

        if command == 1:
            n1 = get_value(program, position + 1, relative_base, params[0])
            n2 = get_value(program, position + 2, relative_base, params[1])

            # Location to write to will always use the immediate value
            location = get_value(program, position + 3, relative_base, Mode.IMMEDIATE)

            if Mode(params[2]) == Mode.RELATIVE:
                location += relative_base

            program = write_value(program, location, n1 + n2)
            position += 4

        elif command == 2:
            n1 = get_value(program, position + 1, relative_base, params[0])
            n2 = get_value(program, position + 2, relative_base, params[1])

            # Location to write to will always use the immediate value
            location = get_value(program, position + 3, relative_base, Mode.IMMEDIATE)

            if Mode(params[2]) == Mode.RELATIVE:
                location += relative_base

            program = write_value(program, location, n1 * n2)
            position += 4

        elif command == 3:
            # Location to write to will always use the immediate value
            location = get_value(program, position + 1, relative_base, Mode.IMMEDIATE)

            if Mode(params[0]) == Mode.RELATIVE:
                location += relative_base

            program = write_value(program, location, input[input_counter])
            input_counter += 1
            position += 2

        elif command == 4:
            value = get_value(program, position + 1, relative_base, params[0])
            outputs.append(value)
            position += 2

            # In a feedback loop we want to preserve our current progress
            if feedback:
                return program, outputs, position

        elif command == 5:
            to_check = get_value(program, position + 1, relative_base, params[0])
            new_position = get_value(program, position + 2, relative_base, params[1])

            if to_check != 0:
                position = new_position
            else:
                position += 3

        elif command == 6:
            to_check = get_value(program, position + 1, relative_base, params[0])
            new_position = get_value(program, position + 2, relative_base, params[1])

            if to_check == 0:
                position = new_position
            else:
                position += 3

        elif command == 7:
            p1 = get_value(program, position + 1, relative_base, params[0])
            p2 = get_value(program, position + 2, relative_base, params[1])

            # Location to write to will always use the immediate value
            location = get_value(program, position + 3, relative_base, Mode.IMMEDIATE)

            if Mode(params[2]) == Mode.RELATIVE:
                location += relative_base

            if p1 < p2:
                program = write_value(program, location, 1)
            else:
                program = write_value(program, location, 0)

            position += 4

        elif command == 8:
            p1 = get_value(program, position + 1, relative_base, params[0])
            p2 = get_value(program, position + 2, relative_base, params[1])

            # Location to write to will always use the immediate value
            location = get_value(program, position + 3, relative_base, Mode.IMMEDIATE)

            if Mode(params[2]) == Mode.RELATIVE:
                location += relative_base

            if p1 == p2:
                program = write_value(program, location, 1)
            else:
                program = write_value(program, location, 0)

            position += 4

        elif command == 9:
            base = get_value(program, position + 1, relative_base, params[0])

            relative_base += base
            position += 2

    return program, outputs, position
