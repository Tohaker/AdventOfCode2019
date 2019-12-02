def part_one():
    total = 0

    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]

    for line in lines:
        total += (int(int(line) / 3) - 2)

    return total


def part_two():
    with open('input.txt', 'r') as file:
        lines = [line.rstrip('\n') for line in file]

    total = 0

    for line in lines:
        total += calculate_module_fuel(int(line))

    return total


def calculate_module_fuel(starting_mass):
    total = 0
    fuel_mass = starting_mass

    while fuel_mass > 0:
        fuel_mass = (int(int(fuel_mass) / 3) - 2)

        if fuel_mass < 0:
            fuel_mass = 0

        total += fuel_mass

    return total


if __name__ == '__main__':
    print(part_one())
    print(part_two())
