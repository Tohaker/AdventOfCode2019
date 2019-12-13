import copy
import math


def apply_gravity(moons):
    apply_gravity_single_coordinate(moons, 0)
    apply_gravity_single_coordinate(moons, 1)
    apply_gravity_single_coordinate(moons, 2)


def apply_gravity_single_coordinate(moons, variable):
    for moon in moons:
        for other_moon in moons:
            if other_moon != moon:
                if moon[0][variable] < other_moon[0][variable]:
                    moon[1][variable] += 1
                elif moon[0][variable] > other_moon[0][variable]:
                    moon[1][variable] -= 1


def apply_velocity(moons):
    apply_velocity_single_coordinate(moons, 0)
    apply_velocity_single_coordinate(moons, 1)
    apply_velocity_single_coordinate(moons, 2)


def apply_velocity_single_coordinate(moons, variable):
    for moon in moons:
        moon[0][variable] += moon[1][variable]


def part_one(moons):
    for i in range(1000):
        apply_gravity(moons)
        apply_velocity(moons)

    total = 0
    for moon in moons:
        pot = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
        kin = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
        total += pot * kin

    return total


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# Counting to the first 0 velocity and multiplying by 2.
def part_two(moons):
    initial = copy.deepcopy([moons[0][1], moons[1][1], moons[2][1], moons[3][1]])
    result = []
    for variable in range(3):
        count = 0
        while True:
            apply_gravity_single_coordinate(moons, variable)
            apply_velocity_single_coordinate(moons, variable)
            count += 1

            new = [moons[0][1], moons[1][1], moons[2][1], moons[3][1]]
            # print(new)

            if new == initial and count > 1:
                result.append(count * 2)
                break

    total = lcm(result[2], lcm(result[0], result[1]))
    return total


if __name__ == '__main__':
    # Puzzle Input
    m1 = ([-7, 17, -11], [0, 0, 0])
    m2 = ([9, 12, 5], [0, 0, 0])
    m3 = ([-9, 0, -4], [0, 0, 0])
    m4 = ([4, 6, 0], [0, 0, 0])

    # Example 1
    # m1 = ([-1, 0, 2], [0, 0, 0])
    # m2 = ([2, -10, -7], [0, 0, 0])
    # m3 = ([4, -8, 8], [0, 0, 0])
    # m4 = ([3, 5, -1], [0, 0, 0])

    # Example 2
    # m1 = ([-8, -10, 0], [0, 0, 0])
    # m2 = ([5, 5, 10], [0, 0, 0])
    # m3 = ([2, -7, 3], [0, 0, 0])
    # m4 = ([9, -8, -3], [0, 0, 0])

    print(part_one(copy.deepcopy([m1, m2, m3, m4])))
    print(part_two([m1, m2, m3, m4]))
