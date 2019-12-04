def check_valid_password_part_one(password):
    return adjacent_digits_equal(password) and decreasing_digits(password)


def check_valid_password_part_two(password):
    return adjacent_digits_equal_and_only_two(password) and decreasing_digits(password)


def adjacent_digits_equal(password):
    p = str(password)
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            return True

    return False


def adjacent_digits_equal_and_only_two(password):
    p = str(password)
    return 2 in map(p.count, p)


def decreasing_digits(password):
    p = str(password)
    for i in range(len(p) - 1):
        if int(p[i]) > int(p[i + 1]):
            return False

    return True


def part_one():
    max = 748759
    min = 284639

    current = min

    valid_passwords = []

    while current <= max:
        if check_valid_password_part_one(current):
            valid_passwords.append(current)
        current += 1

    return len(valid_passwords)


def part_two():
    max = 748759
    min = 284639

    current = min

    valid_passwords = []

    while current <= max:
        if check_valid_password_part_two(current):
            valid_passwords.append(current)
        current += 1

    return len(valid_passwords)


if __name__ == '__main__':
    print(part_one())
    print(part_two())
