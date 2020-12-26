from intcode import run_computer


class TestIntcode:
    def test_intcode_day_two(self):
        program = ['1', '9', '10', '3', '2', '3',
                   '11', '0', '99', '30', '40', '50']
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        result = run_computer(program)
        assert result == expected

        program = ['1', '0', '0', '0', '99']
        expected = [2, 0, 0, 0, 99]
        result = run_computer(program)
        assert result == expected

        program = ['2', '3', '0', '3', '99']
        expected = [2, 3, 0, 6, 99]
        result = run_computer(program)
        assert result == expected

        program = ['2', '4', '4', '5', '99', '0']
        expected = [2, 4, 4, 5, 99, 9801]
        result = run_computer(program)
        assert result == expected

        program = ['1', '1', '1', '4', '99', '5', '6', '0', '99']
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        result = run_computer(program)
        assert result == expected
