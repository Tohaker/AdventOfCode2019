import math


def parse_input(input):
    asteroid_map = [s.strip() for s in input]
    rows, cols = len(asteroid_map), len(asteroid_map[0])

    asteroids = set()
    for i in range(rows):
        for j in range(cols):
            if asteroid_map[i][j] == "#":
                asteroids.add((i, j))

    return asteroids


def count_visible_asteroids(station, asteroids):
    detected = set()
    for asteroid in asteroids:
        if asteroid != station:
            dx, dy = asteroid[0] - station[0], asteroid[1] - station[1]
            g = abs(math.gcd(dx, dy))
            reduced = (dx // g, dy // g)
            detected.add(reduced)
    return detected


def part_one(input):
    asteroids = parse_input(input)

    return max(map(lambda station: len(count_visible_asteroids(station, asteroids)), asteroids))


def part_two(input):
    asteroids = list(parse_input(input))

    count_map = list(
        map(lambda station: len(count_visible_asteroids(station, asteroids)), asteroids)
    )

    # Find the station that corresponds to the max count of visible asteroids.
    station = asteroids[count_map.index(max(count_map))]
    map_to_destroy = count_visible_asteroids(station, asteroids)

    # Find the angles to each asteroid, and find the first 200 to destroy
    destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in map_to_destroy]
    destroyed.sort(reverse=True)
    dx, dy = destroyed[200 - 1][1]

    #  Loop around the asteroids until all 200 are destroyed
    x, y = station[0] + dx, station[1] + dy
    while (x, y) not in asteroids:
        x, y = x + dx, y + dy

    return y * 100 + x