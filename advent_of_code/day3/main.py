def find_covered_points(wire):
    wire_points = []

    x = 0
    y = 0

    for command in wire:
        direction = command[:1]
        distance = int(command[1:]) + 1

        if direction == 'U':
            for i in range(distance):
                wire_points.append(
                    ((x, y + i), i))
        elif direction == 'R':
            for i in range(distance):
                wire_points.append(
                    ((x + i, y), i))
        elif direction == 'L':
            for i in range(distance):
                wire_points.append(
                    ((x - i, y), i))
        else:
            for i in range(distance):
                wire_points.append(
                    ((x, y - i), i))

        # Get the final X,Y coordinates from this command.
        x = wire_points[len(wire_points) - 1][0][0]
        y = wire_points[len(wire_points) - 1][0][1]

    return wire_points


def wire_length_to_intercept(wire1, wire2, intercept):
    # As intercepts doesn't contain the rest of the dictionary, we
    # go to find it by searching for the coordinate in the original list
    w1_index = next(i for i, item in enumerate(wire1) if item[0] == intercept)
    w2_index = next(i for i, item in enumerate(wire2) if item[0] == intercept)

    # The result is the combined length of each array of steps
    # where progress has been made.
    wire1_length = len(
        list(filter(lambda d: d[1] != 0, wire1[:w1_index + 1])))
    wire2_length = len(
        list(filter(lambda d: d[1] != 0, wire2[:w2_index + 1])))

    return wire1_length + wire2_length


def part_one(input):
    # Input consists of 2 lines
    wire1 = find_covered_points(input[0].split(','))
    wire2 = find_covered_points(input[1].split(','))

    intercepts = set([w[0] for w in wire1]) & set(
        [w[0] for w in wire2])

    return min(filter(bool, map(lambda intercept: abs(intercept[0]) + abs(intercept[1]), intercepts)))


def part_two(input):
    # Input consists of 2 lines
    wire1 = find_covered_points(input[0].split(','))
    wire2 = find_covered_points(input[1].split(','))

    intercepts = set([w[0] for w in wire1]) & set([w[0] for w in wire2])

    return min(filter(bool, map(lambda intercept: wire_length_to_intercept(wire1, wire2, intercept), intercepts)))
