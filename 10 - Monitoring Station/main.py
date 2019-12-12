import ast
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


def determine_distance_to_asteroid(a1, a2):
    return math.sqrt(math.pow(a2['x'] - a1['x'], 2) + math.pow(a2['y'] - a1['y'], 2))


def find_visible_asteroids(coords, base):
    base = ast.literal_eval(base)
    angles = {}

    for asteroid in coords:
        if asteroid['x'] == base['x'] and asteroid['y'] == base['y']:
            coords.remove(asteroid)
        else:
            angle = determine_angle_to_asteroid(base, asteroid)
            if angle in angles:
                angles[angle].append(asteroid)
            else:
                angles[angle] = [asteroid]

    for angle in angles.items():
        closest = 1000000
        for asteroid in angle[1]:
            d = determine_distance_to_asteroid(base, asteroid)
            if d < closest:
                closest = d
                closest_asteroid = asteroid

        angles[angle[0]] = closest_asteroid

    return angles


def part_two(base):
    coords = coordinates_of_asteroids(read_input())
    order_of_elimination = []

    while len(coords) > 0:
        v = {angle: asteroid for angle, asteroid in
             sorted(find_visible_asteroids(coords, base).items(), key=lambda item: item[0])}

        for a, asteroid in v.items():
            coords.remove(asteroid)
            order_of_elimination.append(asteroid)

    return order_of_elimination[199]['x'] * 100 + order_of_elimination[199]['y']


if __name__ == '__main__':
    l, c = part_one()
    print('Answer: {}'.format(part_two(c)))
