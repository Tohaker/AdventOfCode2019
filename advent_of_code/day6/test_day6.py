from day6 import part_one, part_two


class TestDay6:
    def test_part_one(self):
        input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G',
                 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
        assert part_one(input) == 42

    def test_part_two(self):
        input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G',
                 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
        assert part_two(input) == 4
