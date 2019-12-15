import math


def read_input():
    with open('test_input.txt', 'r') as file:
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


def calculate_requirements(desired_result, desired_quantity, reactions, total_ore, waste):
    requirements = list(filter(lambda r: r[1][1] == desired_result, reactions))[0]

    if 'ORE' in requirements[0][0][1]:
        reaction_quantity = int(requirements[0][0][0])
        requirement_quantity = int(requirements[1][0])

        # Check if we have enough waste to cover the quantity needed.
        if requirements[1][1] in waste and waste[requirements[1][1]] >= desired_quantity:
            waste[requirements[1][1]] -= desired_quantity
            return total_ore, waste

        # Check if we're producing more than we need. Put it into waste.
        if requirement_quantity > desired_quantity:
            if requirements[1][1] not in waste:
                waste[requirements[1][1]] = reaction_quantity - desired_quantity
            else:
                waste[requirements[1][1]] += reaction_quantity - desired_quantity

        if requirement_quantity < desired_quantity:
            factor = math.ceil(desired_quantity / requirement_quantity)
            new_ore = reaction_quantity * factor
            return total_ore + new_ore, waste

        return total_ore + reaction_quantity, waste

    for r in requirements[0]:
        reactions_needed = math.ceil(desired_quantity / int(r[0]))
        desired_quantity = int(r[0]) * reactions_needed
        desired_result = r[1]
        total_ore, waste = calculate_requirements(desired_result, desired_quantity, reactions, total_ore, waste)

    return total_ore, waste


def calculate_requirements_2(reactions, desired_result, desired_quantity, total_ore, waste):
    requirements = list(filter(lambda r: r[1][1] == desired_result, reactions))[0]

    result_quantity = int(requirements[1][0])
    factor = math.ceil((desired_quantity - waste[desired_result]) / result_quantity)

    if 'ORE' in requirements[0][0][1]:
        # Check if we're producing more than we need. Put it into waste.
        amount_to_be_made = result_quantity * factor
        if desired_quantity < amount_to_be_made:
            waste[desired_result] += amount_to_be_made - desired_quantity

        # Check if we used any waste, and remove it from the store.
        if amount_to_be_made < desired_quantity:
            waste[desired_result] = waste[desired_result] - (desired_quantity - amount_to_be_made)

        # Check if we have enough waste to cover the quantity needed.
        if desired_result in waste and waste[desired_result] >= desired_quantity:
            waste[desired_result] -= desired_quantity
        else:
            reaction_quantity = int(requirements[0][0][0])
            total_ore += reaction_quantity * factor

        return total_ore, waste

    for ingredient in requirements[0]:
        ingredient_quantity = int(ingredient[0]) * factor
        desired_result = ingredient[1]

        total_ore, waste = calculate_requirements_2(reactions, desired_result, ingredient_quantity, total_ore, waste)

    return total_ore, waste


def part_one():
    reactions = read_input()

    # Find out which reactions require ore.
    requirements = list(filter(lambda r: r[0][0][1] == 'ORE', reactions))

    waste = {element[1][1]: 0 for element in reactions}

    # return calculate_requirements('FUEL', 1, reactions, 0, {})[0]
    return calculate_requirements_2(reactions, 'FUEL', 1, 0, waste)[0]


if __name__ == '__main__':
    print(part_one())
