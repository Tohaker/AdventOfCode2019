import copy


def read_file():
    with open('input.txt', 'r') as file:
        return [line.rstrip('\n') for line in file]


def determine_orbital_relationships(input):
    orbital_relationships = []

    for orbit in input:
        parent, child = orbit.split(')')
        orbital_relationships.append({'parent': parent, 'child': child})

    return orbital_relationships


def part_one(input):
    print(input)

    # Each line is a direct orbit
    direct_orbits = len(input)
    indirect_orbits = 0

    orbital_relationships = determine_orbital_relationships(input)

    for relationship in orbital_relationships:
        r = copy.copy(relationship)
        child = r['child']
        print('Orbits for {}'.format(child))
        reached_com = r['parent'] == 'COM'

        while not reached_com:
            indirect_orbits += 1
            child = r['parent']
            r = [item for item in orbital_relationships if item.get('child') == child][0]
            reached_com = r['parent'] == 'COM'

    return direct_orbits + indirect_orbits


def find_orbit_intersect(santa_orbit, your_orbit):
    intersect = 'COM'

    for so in santa_orbit:
        for yo in your_orbit:
            if so is yo:
                return so

    return intersect


# Find the chain from YOU to COM and SAN to COM.
# Find the closest common planet.
# Find the number of indirect orbits to that planet from SAN and YOU.
# Add together the numbers.
def part_two(input):
    orbital_relationships = determine_orbital_relationships(input)

    you_current = [item['parent'] for item in orbital_relationships if item.get('child') == 'YOU'][0]
    san_current = [item['parent'] for item in orbital_relationships if item.get('child') == 'SAN'][0]

    you_reached_com = you_current == 'COM'
    san_reached_com = san_current == 'COM'

    you_orbits = []
    san_orbits = []

    while not you_reached_com:
        you_orbits.append(you_current)
        r = [item for item in orbital_relationships if item.get('child') == you_current][0]
        you_current = r['parent']
        you_reached_com = you_current == 'COM'

    while not san_reached_com:
        san_orbits.append(san_current)
        r = [item for item in orbital_relationships if item.get('child') == san_current][0]
        san_current = r['parent']
        san_reached_com = san_current == 'COM'

    intersect = find_orbit_intersect(san_orbits, you_orbits)

    you_indirect_orbits = you_orbits.index(intersect) - 1
    san_indirect_orbits = san_orbits.index(intersect) - 1

    return you_indirect_orbits + san_indirect_orbits


if __name__ == '__main__':
    print(part_one(read_file()))
    print(part_two(read_file()))
