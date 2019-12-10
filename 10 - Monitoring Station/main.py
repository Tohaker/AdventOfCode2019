import math


def read_input():
    with open('test_input.txt', 'r') as file:
        return list([list(line.rstrip('\n')) for line in file])


def coordinates_of_asteroids(input):
    coords = []

    for y, line in enumerate(input):
        for x, point in enumerate(line):
            if point == '#':
                coords.append({'x': x, 'y': y})

    return coords


# y = mx + c -> m = (y - c)/x
def determine_points_on_line(point_1, point_2, max_x, max_y):
    x1 = point_1['x']
    y1 = point_1['y']

    x2 = point_2['x']
    y2 = point_2['y']

    output = []

    if x1 - x2 != 0:
        m = (y2 - y1) / (x2 - x1)
        for x in range(max_x + 1):
            interpolant = y1 + (x - x1) * m
            output.append({'x': x, 'y': interpolant})
    else:
        m = 0
        for y in range(max_y + 1):
            interpolant = x1
            output.append({'x': interpolant, 'y': y})

    return output


def determine_asteroids_on_path(map, path):
    on_path = []

    for point in path:
        for asteroid in map:
            if asteroid['x'] == point['x'] and asteroid['y'] == point['y']:
                on_path.append(asteroid)

    return on_path


def get_closest_asteroid(origin, asteroids):
    closest = 10000000
    for a in asteroids:
        d = math.sqrt((math.pow(a['x'] - origin['x'], 2) + math.pow(a['y'] - origin['y'], 2)))
        if d < closest:
            closest = d
            chosen = a

    return chosen


def part_one():
    c = coordinates_of_asteroids(read_input())

    max_x = 0
    max_y = 0
    for point in c:
        if point['x'] > max_x:
            max_x = point['x']
        if point['y'] > max_y:
            max_y = point['y']

    asteroids = {}

    for i, coord in enumerate(c):
        visible = []
        print(coord)
        for asteroid in c:
            if asteroid['x'] == coord['x'] and asteroid['y'] == coord['y']:
                continue
            else:
                p = determine_points_on_line(coord, asteroid, max_x, max_y)
                d = determine_asteroids_on_path(c, p)
                if coord in d:
                    d.remove(coord)
                if len(d) != 0 and d not in visible:
                    visible.append(d)

        asteroids[str(c[i])] = visible

    return asteroids


if __name__ == '__main__':
    p = part_one()
    largest = 0
    for i in p:
        if len(p[i]) > largest:
            largest = len(p[i])

    print(largest)
