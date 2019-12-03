import multiprocessing


def read_wire_paths():
    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]

    w1 = lines[0].split(',')
    w2 = lines[1].split(',')

    return w1, w2


def calculate_points(wire):
    wire_points = []

    x = 0
    y = 0

    for j, command in enumerate(wire):
        direction = command[:1]
        distance = int(command[1:])

        for i in range(distance + 1):
            if direction == 'U':
                wire_points.append({'coord': [x, y + i], 'command': j, 'completion': i})
            elif direction == 'R':
                wire_points.append({'coord': [x + i, y], 'command': j, 'completion': i})
            elif direction == 'L':
                wire_points.append({'coord': [x - i, y], 'command': j, 'completion': i})
            else:
                wire_points.append({'coord': [x, y - i], 'command': j, 'completion': i})

        # Get the final X,Y coordinates from this command.
        x = wire_points[len(wire_points) - 1]['coord'][0]
        y = wire_points[len(wire_points) - 1]['coord'][1]

    return wire_points


def calculate_intercepts(w1, w2):
    intercepts = []

    for point_1 in w1:
        for point_2 in w2:
            if point_1['coord'][0] == point_2['coord'][0] and point_1['coord'][1] == point_2['coord'][1]:
                print('Found intercept: ' + str(point_1['coord'][0]) + ' , ' + str(point_1['coord'][1]))
                intercepts.append([point_1, point_2])

    return intercepts


def calculate_intercepts_multiprocess(w1, w2, return_list, process_number):
    intercepts = return_list[process_number]

    print('Thread {} started'.format(process_number))

    for point_1 in w1:
        for point_2 in w2:
            if point_1['coord'][0] == point_2['coord'][0] and point_1['coord'][1] == point_2['coord'][1]:
                print('Found intercept: ' + str(point_1['coord'][0]) + ' , ' + str(point_1['coord'][1]))
                intercepts.append([point_1, point_2])

    print('Thread {} returned'.format(process_number))

    return intercepts


# We should calculate all the points at which each line covers.
# Then find the common points.
# Then find the lowest Manhattan Distance (x + y)
def part_one():
    wire_1, wire_2 = read_wire_paths()

    x = 0
    y = 0

    wire_1_points = calculate_points(wire_1)
    wire_2_points = calculate_points(wire_2)

    # manager = multiprocessing.Manager()
    # return_list = manager.list()
    # jobs = []
    #
    # split_wire_points = []
    # n = int(len(wire_2_points) / 4)
    # for i in range(0, len(wire_2_points), n):
    #     split_wire_points.append(wire_2_points[i:i + n])
    #     return_list.append([])
    #
    # for i in range(len(split_wire_points)):
    #     p = multiprocessing.Process(target=calculate_intercepts_multiprocess,
    #                                 args=(wire_1_points, split_wire_points[i], return_list, i))
    #     jobs.append(p)
    #     p.start()
    #
    # for process in jobs:
    #     process.join()
    #
    # intercepts = return_list

    intercepts = calculate_intercepts(wire_1_points, wire_2_points)

    lowest = 10000000000000

    for intercept in intercepts:
        x = abs(intercept[0]['coord'][0])
        y = abs(intercept[0]['coord'][1])

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

    wire_1_points = calculate_points(wire_1)
    wire_2_points = calculate_points(wire_2)

    intercepts = calculate_intercepts(wire_1_points, wire_2_points)

    print('Found {} intercepts'.format(len(intercepts)))

    lowest = 1000000000000

    # Here we get the route up until this intersection
    for intercept in intercepts:
        route_wire_1 = wire_1[:intercept[0]['command'] + 1]
        route_wire_2 = wire_2[:intercept[1]['command'] + 1]

        wire_1_total = 0
        wire_2_total = 0

        for i, command in enumerate(route_wire_1):
            if i < len(route_wire_1) - 1:
                wire_1_total += int(command[1:])
            else:
                wire_1_total += int(intercept[0]['completion'])

        for i, command in enumerate(route_wire_2):
            if i < len(route_wire_2) - 1:
                wire_2_total += int(command[1:])
            else:
                wire_2_total += int(intercept[1]['completion'])

        signal_delay = wire_1_total + wire_2_total

        print('Signal Delay: {}'.format(signal_delay))

        if signal_delay < lowest and signal_delay != 0:
            lowest = signal_delay

    return lowest


if __name__ == '__main__':
    print(part_one())
