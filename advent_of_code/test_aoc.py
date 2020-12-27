from lib.get_input import download_input
import day1
import day2
import day3
import day4
import day5


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
