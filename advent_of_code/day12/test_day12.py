from day12 import part_one, part_two


class TestDay12:
    def test_part_one(self):
        input = ["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>", "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"]
        assert part_one(input, 10) == 179

        input = ["<x=-8, y=-10, z=0>", "<x=5, y=5, z=10>", "<x=2, y=-7, z=3>", "<x=9, y=-8, z=-3>"]
        assert part_one(input, 100) == 1940

    def test_part_two(self):
        input = ["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>", "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"]
        assert part_two(input) == 2772

        input = ["<x=-8, y=-10, z=0>", "<x=5, y=5, z=10>", "<x=2, y=-7, z=3>", "<x=9, y=-8, z=-3>"]
        assert part_two(input) == 4686774924