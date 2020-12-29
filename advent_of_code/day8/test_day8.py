from day8 import part_one, part_two


class TestDay8:
    def test_part_one(self):
        input = ['123456789012']
        assert part_one(input, 3, 2) == 1

    def test_part_two(self):
        input = ['0222112222120000']
        assert part_two(input, 2, 2) == [[0, 1], [1, 0]]
