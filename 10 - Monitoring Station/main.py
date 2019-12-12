import ast
import math
import numpy as np


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


def determine_angle_to_asteroid(point_1, point_2):
    x1 = point_1['x']
    y1 = point_1['y']

    x2 = point_2['x']
    y2 = point_2['y']

    x = x2 - x1
    y = y2 - y1

    result = math.degrees(math.atan2(y, x)) + 90
    if result < 0:
        return result + 360
    return result


def part_one():
    c = coordinates_of_asteroids(read_input())

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
    chosen = {}
    for i in asteroids:
        if len(asteroids[i]) > largest:
            largest = len(asteroids[i])
            chosen = i

    return largest, chosen


def find_visible_asteroids(coords, base):
    base = ast.literal_eval(base)
    visible = {}
    angles = []

    for asteroid in coords:
        if asteroid['x'] == base['x'] and asteroid['y'] == base['y']:
            coords.remove(asteroid)
        else:
            angle = determine_angle_to_asteroid(base, asteroid)
            if angle not in angles:
                angles.append(angle)
                visible[str(asteroid)] = angle

    return visible


def reorder_by_angle(visible):
    positive = {}
    negative = {}

    for a, angle in visible.items():
        if angle >= 0:
            positive[a] = angle
        if angle < 0:
            negative[a] = angle

    return positive, negative


def part_two(base):
    coords = coordinates_of_asteroids(read_input())
    order_of_elimination = []

    while len(coords) > 0:
        v = {asteroid: angle for asteroid, angle in
             sorted(find_visible_asteroids(coords, base).items(), key=lambda item: item[1])}

        for angle in np.arange(0, 360, 0.00001):
            for asteroid, a in v.items():
                if a == angle:
                    coords.remove(asteroid)
                    order_of_elimination.append(asteroid)

        # p, n = reorder_by_angle(v)
        # for asteroid, angle in p.items():
        #     asteroid = ast.literal_eval(asteroid)
        #     print('Destroyed asteroid at {0}, {1} with angle {2}'.format(asteroid['x'], asteroid['y'], angle))
        #     order_of_elimination.append(asteroid)
        #     coords.remove(asteroid)
        # for asteroid, angle in n.items():
        #     asteroid = ast.literal_eval(asteroid)
        #     print('Destroyed asteroid at {0}, {1} with angle {2}'.format(asteroid['x'], asteroid['y'], angle))
        #     order_of_elimination.append(asteroid)
        #     coords.remove(asteroid)

    return order_of_elimination[200]


if __name__ == '__main__':
    l, c = part_one()
    print(part_two(c))
