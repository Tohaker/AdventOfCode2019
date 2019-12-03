def read_wire_paths():
    with open('test_input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]

    w1 = lines[0].split(',')
    w2 = lines[1].split(',')

    return w1, w2


# We should calculate all the points at which each line covers.
# Then find the common points.
# Then find the lowest Manhattan Distance (x + y)
def part_one():
    wire_1, wire_2 = read_wire_paths()

    x = 0
    y = 0

    wire_1_points = []
    wire_2_points = []

    for command in wire_1:
        direction = command[:1]
        distance = int(command[1:])

        for i in range(distance + 1):
            if direction == 'U':
                wire_1_points.append([x, y + i])
            elif direction == 'R':
                wire_1_points.append([x + i, y])
            elif direction == 'L':
                wire_1_points.append([x - i, y])
            else:
                wire_1_points.append([x, y - i])

        # Get the final X,Y coordinates from this command.
        x = wire_1_points[len(wire_1_points) - 1][0]
        y = wire_1_points[len(wire_1_points) - 1][1]

    x = 0
    y = 0

    for command in wire_2:
        direction = command[:1]
        distance = int(command[1:])

        for i in range(distance + 1):
            if direction == 'U':
                wire_2_points.append([x, y + i])
            elif direction == 'R':
                wire_2_points.append([x + i, y])
            elif direction == 'L':
                wire_2_points.append([x - i, y])
            else:
                wire_2_points.append([x, y - i])

        # Get the final X,Y coordinates from this command.
        x = wire_2_points[len(wire_2_points) - 1][0]
        y = wire_2_points[len(wire_2_points) - 1][1]

    intercepts = []

    for point_1 in wire_1_points:
        for point_2 in wire_2_points:
            if point_1[0] == point_2[0] and point_1[1] == point_2[1]:
                print('Found intercept: ' + str(point_1[0]) + ' , ' + str(point_1[1]))
                intercepts.append(point_1)

    lowest = 10000000000000

    for intercept in intercepts:
        x = abs(intercept[0])
        y = abs(intercept[1])

        manhattan_distance = x + y
        if manhattan_distance != 0 and manhattan_distance < lowest:
            lowest = manhattan_distance

    return lowest


# We have to track the number of steps to each intersection.
# This can be done by tracking the commands along with each step,
# collating a list of unique / non-continuous commands and retracing them
# with each intersection.
def part_two():
    wire_1, wire_2 = read_wire_paths()


if __name__ == '__main__':
    print(part_one())
