import copy


def apply_gravity(moons):
    for moon in moons:
        velocity = moon[1]
        for other_moon in moons:
            if other_moon != moon:
                for i, coordinate in enumerate(moon[0]):
                    if coordinate < other_moon[0][i]:
                        velocity[i] += 1
                    elif coordinate > other_moon[0][i]:
                        velocity[i] -= 1


def apply_velocity(moons):
    for moon in moons:
        for i, coordinate in enumerate(moon[1]):
            moon[0][i] += coordinate


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


# Counting to the first 0 velocity and multiplying by 2.
def part_two(moons):
    initital = copy.deepcopy([moons[0][1], moons[1][1], moons[2][1], moons[3][1]])
    count = 0
    while True:
        apply_gravity(moons)
        apply_velocity(moons)
        count += 1

        new = [moons[0][1], moons[1][1], moons[2][1], moons[3][1]]
        print(new)

        if new == initital and count > 1:
            return count * 2


if __name__ == '__main__':
    # m1 = ([-7, 17, -11], [0, 0, 0])
    # m2 = ([9, 12, 5], [0, 0, 0])
    # m3 = ([-9, 0, -4], [0, 0, 0])
    # m4 = ([4, 6, 0], [0, 0, 0])

    # m1 = ([-1, 0, 2], [0, 0, 0])
    # m2 = ([2, -10, -7], [0, 0, 0])
    # m3 = ([4, -8, 8], [0, 0, 0])
    # m4 = ([3, 5, -1], [0, 0, 0])

    m1 = ([-8, -10, 0], [0, 0, 0])
    m2 = ([5, 5, 10], [0, 0, 0])
    m3 = ([2, -7, 3], [0, 0, 0])
    m4 = ([9, -8, -3], [0, 0, 0])

    # print(part_one([m1, m2, m3, m4]))
    print(part_two([m1, m2, m3, m4]))
