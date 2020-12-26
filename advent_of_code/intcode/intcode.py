def run_computer(program):
    position = 0
    program = list(map(int, program))

    while program[position] != 99:
        command = program[position]

        if command == 1:
            p1 = program[position + 1]
            p2 = program[position + 2]
            n1 = program[p1]
            n2 = program[p2]
            location = program[position + 3]

            program[location] = n1 + n2
            position += 4

        elif command == 2:
            p1 = program[position + 1]
            p2 = program[position + 2]
            n1 = program[p1]
            n2 = program[p2]
            location = program[position + 3]

            program[location] = n1 * n2
            position += 4

    return program
