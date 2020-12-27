from copy import copy


def parse_input(input):
    return list(map(lambda line: (line.split(')')[0], line.split(')')[1]), input))


def part_one(input):
    orbital_relationships = parse_input(input)
    indirect_orbits = 0

    for relationship in orbital_relationships:
        r = copy(relationship)

        while r[0] != 'COM':
            indirect_orbits += 1
            r = [item for item in orbital_relationships if item[1]
                 == r[0]][0]

    return len(input) + indirect_orbits


def part_two(input):
    orbital_relationships = parse_input(input)

    you_current = [item[0]
                   for item in orbital_relationships if item[1] == 'YOU'][0]
    san_current = [item[0]
                   for item in orbital_relationships if item[1] == 'SAN'][0]

    you_orbits = []
    san_orbits = []

    while you_current != 'COM':
        you_orbits.append(you_current)
        r = [item for item in orbital_relationships if item[1] == you_current][0]
        you_current = r[0]

    while san_current != 'COM':
        san_orbits.append(san_current)
        r = [item for item in orbital_relationships if item[1] == san_current][0]
        san_current = r[0]

    intersect = set(you_orbits) & set(san_orbits)

    you_index = min(map(lambda parent: next(
        (i for i, p in enumerate(you_orbits) if parent == p)), intersect))

    san_index = min(map(lambda parent: next(
        (i for i, p in enumerate(san_orbits) if parent == p)), intersect))

    return you_index + san_index
