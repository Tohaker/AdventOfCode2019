from day1 import part_one, part_two


class TestDay1:
    input = ['12', '14', '1969', '100756']

    def test_part_one(self):
        result = part_one(self.input)
        assert result == 2 + 2 + 654 + 33583

    def test_part_two(self):
        result = part_two(self.input)
        assert result == 2 + 2 + 966 + 50346
