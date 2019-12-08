def read_image_input():
    with open('input.txt', 'r') as file:
        return list([line.rstrip('\n') for line in file][0])


def decipher_image(width, height):
    input = read_image_input()
    lines = []
    layers = []

    for i in range(0, len(input), width):
        lines.append(input[i:i + width])

    for i in range(0, len(lines), height):
        layers.append(lines[i:i + height])

    return layers


def part_one():
    image = decipher_image(25, 6)

    lowest_count = 10000000
    lowest_layer = 0

    for i, layer in enumerate(image):
        zero_count = 0
        for line in layer:
            zero_count += line.count('0')

        if zero_count < lowest_count:
            lowest_count = zero_count
            lowest_layer = i

    one_count = 0
    two_count = 0
    for line in image[lowest_layer]:
        one_count += line.count('1')
        two_count += line.count('2')

    return one_count * two_count


def part_two():
    width = 25
    height = 6
    image = decipher_image(width, height)

    final_image = []

    for i in range(height):
        new_row = []
        for j in range(width):
            for layer in image:
                pixel = layer[i][j]
                if pixel == '2':
                    continue
                else:
                    new_row.append(pixel)
                    break
        final_image.append(new_row)

    return final_image


if __name__ == '__main__':
    print(part_one())
    [print(line) for line in part_two()]
