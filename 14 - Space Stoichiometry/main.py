import math


def read_input():
    with open('input.txt', 'r') as file:
        output = []
        for line in file.readlines():
            equation = line.split('=>')
            result = equation[1].strip().split()
            inputs = equation[0].split(',')
            components = []
            for c in inputs:
                components.append((c.split()[0], c.split()[1]))

            output.append((components, result))
    return output


def calculate_requirements(reactions, desired_result, desired_quantity, total_ore, waste):
    requirements = list(filter(lambda r: r[1][1] == desired_result, reactions))[0]

    result_quantity = int(requirements[1][0])
    factor = math.ceil((desired_quantity - waste[desired_result]) / result_quantity)

    # Check if we have enough waste to cover the quantity needed.
    if waste[desired_result] >= desired_quantity:
        waste[desired_result] -= desired_quantity
        return total_ore, waste

    # Check if we're producing more than we need. Put it into waste.
    amount_to_be_made = result_quantity * factor
    if desired_quantity < amount_to_be_made:
        waste[desired_result] += amount_to_be_made - desired_quantity

    # Check if we used any waste, and remove it from the store.
    if amount_to_be_made < desired_quantity:
        waste[desired_result] -= (desired_quantity - amount_to_be_made)

    if 'ORE' in requirements[0][0][1]:
        reaction_quantity = int(requirements[0][0][0])
        total_ore += reaction_quantity * factor

        return total_ore, waste

    for ingredient in requirements[0]:
        ingredient_quantity = int(ingredient[0]) * factor
        desired_result = ingredient[1]

        total_ore, waste = calculate_requirements(reactions, desired_result, ingredient_quantity, total_ore, waste)

    return total_ore, waste


def part_one():
    reactions = read_input()

    waste = {element[1][1]: 0 for element in reactions}

    return calculate_requirements(reactions, 'FUEL', 1, 0, waste)[0]


def part_two():
    reactions = read_input()

    waste = {element[1][1]: 0 for element in reactions}

    start = 0
    increment = 10 ** 10
    while increment >= 1:
        ore_per_fuel = 0
        fuel = start
        while ore_per_fuel <= 10 ** 12:
            fuel += increment
            ore_per_fuel = calculate_requirements(reactions, 'FUEL', fuel, 0, waste)[0]
        start = int(fuel - increment)
        increment /= 10

    return fuel - 1


if __name__ == '__main__':
    print(part_one())
    print(part_two())
