from day4 import part_one, part_two


class TestDay4:
    def test_part_one(self):
        input = ['111111-111111']
        result = part_one(input)
        assert result == 1

        input = ['223450-223450']
        result = part_one(input)
        assert result == 0

        input = ['123789-123789']
        result = part_one(input)
        assert result == 0

    def test_part_two(self):
        input = ['112233-112233']
        result = part_two(input)
        assert result == 1

        input = ['123444-123444']
        result = part_two(input)
        assert result == 0

        input = ['111122-111122']
        result = part_two(input)
        assert result == 1
