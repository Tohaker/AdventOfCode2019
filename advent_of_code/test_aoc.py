from lib.get_input import download_input
import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10


class TestAOCSolutions:
    def test_day_one(self):
        input = download_input(1)
        assert day1.part_one(input) == 3317970
        assert day1.part_two(input) == 4974073

    def test_day_two(self):
        input = download_input(2)
        assert day2.part_one(input) == 3850704
        assert day2.part_two(input) == 6718

    def test_day_three(self):
        input = download_input(3)
        assert day3.part_one(input) == 651
        assert day3.part_two(input) == 7534

    def test_day_four(self):
        input = download_input(4)
        assert day4.part_one(input) == 895
        assert day4.part_two(input) == 591

    def test_day_five(self):
        input = download_input(5)
        assert day5.part_one(input) == 10987514
        assert day5.part_two(input) == 14195011

    def test_day_six(self):
        input = download_input(6)
        assert day6.part_one(input) == 251208
        assert day6.part_two(input) == 397

    def test_day_seven(self):
        input = download_input(7)
        assert day7.part_one(input) == 21000
        assert day7.part_two(input) == 61379886

    def test_day_eight(self):
        input = download_input(8)
        assert day8.part_one(input) == 1560
        assert day8.part_two(input) == [
            [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
            [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
        ]

    def test_day_nine(self):
        input = download_input(9)
        assert day9.part_one(input) == 3100786347
        assert day9.part_two(input) == 87023

    def test_day_ten(self):
        input = download_input(10)
        assert day10.part_one(input) == 309
        assert day10.part_two(input) == 416