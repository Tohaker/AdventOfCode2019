def single_module_fuel(mass):
    return (int(int(mass) / 3) - 2)


def calculate_module_fuel(starting_mass):
    total = 0
    fuel_mass = int(starting_mass)

    while fuel_mass > 0:
        fuel_mass = single_module_fuel(fuel_mass)

        if fuel_mass < 0:
            fuel_mass = 0
            break

        total += fuel_mass

    return total


def part_one(input):
    return sum(map(lambda mass: single_module_fuel(mass), input))


def part_two(input):
    return sum(map(lambda mass: calculate_module_fuel(mass), input))
