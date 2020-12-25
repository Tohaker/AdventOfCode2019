from lib.get_input import download_input
import day1


class TestAOCSolutions:
    def test_day_one(self):
        input = download_input(1)
        assert day1.part_one(input) == 3317970
        assert day1.part_two(input) == 4974073
