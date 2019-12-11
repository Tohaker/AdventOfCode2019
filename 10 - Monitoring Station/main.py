import math


def read_input():
    with open('input.txt', 'r') as file:
        return list([list(line.rstrip('\n')) for line in file])


def coordinates_of_asteroids(input):
    coords = []

    for y, line in enumerate(input):
        for x, point in enumerate(line):
            if point == '#':
                coords.append({'x': x, 'y': y})

    return coords


def determine_angle_to_asteroid(point_1, point_2):
    x1 = point_1['x']
    y1 = point_1['y']

    x2 = point_2['x']
    y2 = point_2['y']

    x = x2 - x1
    y = y2 - y1

    return math.atan2(y, x)


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
        angles = []
        print(coord)
        for asteroid in c:
            if asteroid['x'] == coord['x'] and asteroid['y'] == coord['y']:
                continue
            else:
                angle = determine_angle_to_asteroid(coord, asteroid)
                if angle not in angles:
                    angles.append(angle)
                    visible.append({str(asteroid): angle})

        asteroids[str(c[i])] = visible

    largest = 0
    for i in p:
        if len(p[i]) > largest:
            largest = len(p[i])

    return largest


if __name__ == '__main__':
    print(part_one())
