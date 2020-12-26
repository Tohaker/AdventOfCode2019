from lib.get_input import download_input
import day1
import day2


class TestAOCSolutions:
    def test_day_one(self):
        input = download_input(1)
        assert day1.part_one(input) == 3317970
        assert day1.part_two(input) == 4974073

    def test_day_two(self):
        input = download_input(2)
        assert day2.part_one(input) == 3850704
        assert day2.part_two(input) == 6718
