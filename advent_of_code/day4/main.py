import re


def adjacent_digits_equal(password):
    return re.search(r'(\d)\1+', str(password)) is not None


def two_equal_adjacent_digits(password):
    p = str(password)
    return 2 in map(p.count, p)


def has_increasing_digits(password):
    p = str(password)
    for i in range(len(p) - 1):
        if int(p[i]) > int(p[i + 1]):
            return False

    return True


def part_one(input):
    password_range = input[0].split('-')
    min = int(password_range[0])
    max = int(password_range[1])

    valid = []
    for password in range(min, max + 1):
        if adjacent_digits_equal(password) and has_increasing_digits(password):
            valid.append(password)

    return len(valid)


def part_two(input):
    password_range = input[0].split('-')
    min = int(password_range[0])
    max = int(password_range[1])

    valid = []
    for password in range(min, max + 1):
        if two_equal_adjacent_digits(password) and has_increasing_digits(password):
            valid.append(password)

    return len(valid)
