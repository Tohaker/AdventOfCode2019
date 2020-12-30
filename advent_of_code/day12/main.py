from copy import deepcopy
import math


def parse_input(input):
    moons = []

    for line in input:
        coords = line.strip()[1:-1].split(", ")
        x = int(coords[0][2:])
        y = int(coords[1][2:])
        z = int(coords[2][2:])

        moons.append(([x, y, z], [0, 0, 0]))

    return moons


def apply_gravity_single_coordinate(moons, i):
    for moon in moons:
        for other_moon in filter(lambda m: m != moon, moons):
            if moon[0][i] < other_moon[0][i]:
                moon[1][i] += 1
            elif moon[0][i] > other_moon[0][i]:
                moon[1][i] -= 1


def apply_velocity_single_coordinate(moons, i):
    for moon in moons:
        moon[0][i] += moon[1][i]


def apply_gravity(moons):
    for i in range(len(moons[0][0])):
        apply_gravity_single_coordinate(moons, i)


def apply_velocity(moons):
    for i in range(len(moons[0][0])):
        apply_velocity_single_coordinate(moons, i)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part_one(input, steps=1000):
    moons = parse_input(input)

    for _ in range(steps):
        apply_gravity(moons)
        apply_velocity(moons)

    total = 0
    for moon in moons:
        pot = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
        kin = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
        total += pot * kin

    return total


def part_two(input):
    moons = parse_input(input)

    initial_state = deepcopy([moons[0][1], moons[1][1], moons[2][1], moons[3][1]])

    result = []
    for i in range(len(moons[0][0])):
        count = 0
        while True:
            apply_gravity_single_coordinate(moons, i)
            apply_velocity_single_coordinate(moons, i)
            count += 1

            new = [moons[0][1], moons[1][1], moons[2][1], moons[3][1]]

            if new == initial_state and count > 1:
                result.append(count * 2)
                break

    total = lcm(result[2], lcm(result[0], result[1]))
    return total