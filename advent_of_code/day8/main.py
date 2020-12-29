def parse_input(input, w, h):
    lines = []
    layers = []

    for i in range(0, len(input), w):
        lines.append(input[i: i + w])

    for i in range(0, len(lines), h):
        layers.append(lines[i: i + h])

    return layers


def part_one(input, w=25, h=6):
    image = parse_input(input[0], w, h)

    layer_counts = list(map(lambda layer: sum(
        [line.count('0') for line in layer]), image))
    lowest_layer = layer_counts.index(min(layer_counts))

    one_count = 0
    two_count = 0
    for line in image[lowest_layer]:
        one_count += line.count('1')
        two_count += line.count('2')

    return one_count * two_count


def part_two(input, w=25, h=6):
    image = parse_input(input[0], w, h)

    final_image = []

    for i in range(h):
        new_row = []
        for j in range(w):
            for layer in image:
                pixel = layer[i][j]
                if pixel == '2':
                    continue
                else:
                    new_row.append(int(pixel))
                    break
        final_image.append(new_row)

    [print(line) for line in final_image]
    return final_image
