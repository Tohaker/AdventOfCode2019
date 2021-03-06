from intcode import run_computer


class TestIntcode:
    def test_intcode_day_two(self):
        program = ["1", "9", "10", "3", "2", "3", "11", "0", "99", "30", "40", "50"]
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        result = run_computer(program)[0]
        assert result == expected

        program = ["1", "0", "0", "0", "99"]
        expected = [2, 0, 0, 0, 99]
        result = run_computer(program)[0]
        assert result == expected

        program = ["2", "3", "0", "3", "99"]
        expected = [2, 3, 0, 6, 99]
        result = run_computer(program)[0]
        assert result == expected

        program = ["2", "4", "4", "5", "99", "0"]
        expected = [2, 4, 4, 5, 99, 9801]
        result = run_computer(program)[0]
        assert result == expected

        program = ["1", "1", "1", "4", "99", "5", "6", "0", "99"]
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        result = run_computer(program)[0]
        assert result == expected

    def test_intcode_day_five(self):
        program = ["3", "0", "4", "0", "99"]
        input = 25
        result = run_computer(program, [input])[1]
        assert result == [input]

        program = ["1002", "4", "3", "4", "33"]
        expected = [1002, 4, 3, 4, 99]
        result = run_computer(program)[0]
        assert result == expected

        program = ["1101", "100", "-1", "4", "0"]
        expected = [1101, 100, -1, 4, 99]
        result = run_computer(program)[0]
        assert result == expected

        program = [
            "3",
            "12",
            "6",
            "12",
            "15",
            "1",
            "13",
            "14",
            "13",
            "4",
            "13",
            "99",
            "-1",
            "0",
            "1",
            "9",
        ]
        assert run_computer(program, [0])[1][0] == 0
        assert run_computer(program, [8])[1][0] == 1

        program = ["3", "3", "1105", "-1", "9", "1101", "0", "0", "12", "4", "12", "99", "1"]
        assert run_computer(program, [0])[1][0] == 0
        assert run_computer(program, [8])[1][0] == 1

        program = ["3", "9", "8", "9", "10", "9", "4", "9", "99", "-1", "8"]
        assert run_computer(program, [8])[1][0] == 1
        assert run_computer(program, [9])[1][0] == 0

        program = ["3", "9", "7", "9", "10", "9", "4", "9", "99", "-1", "8"]
        assert run_computer(program, [7])[1][0] == 1
        assert run_computer(program, [9])[1][0] == 0

        program = ["3", "3", "1108", "-1", "8", "3", "4", "3", "99"]
        assert run_computer(program, [8])[1][0] == 1
        assert run_computer(program, [9])[1][0] == 0

        program = ["3", "3", "1107", "-1", "8", "3", "4", "3", "99"]
        assert run_computer(program, [7])[1][0] == 1
        assert run_computer(program, [9])[1][0] == 0

        program = [
            "3",
            "21",
            "1008",
            "21",
            "8",
            "20",
            "1005",
            "20",
            "22",
            "107",
            "8",
            "21",
            "20",
            "1006",
            "20",
            "31",
            "1106",
            "0",
            "36",
            "98",
            "0",
            "0",
            "1002",
            "21",
            "125",
            "20",
            "4",
            "20",
            "1105",
            "1",
            "46",
            "104",
            "999",
            "1105",
            "1",
            "46",
            "1101",
            "1000",
            "1",
            "20",
            "4",
            "20",
            "1105",
            "1",
            "46",
            "98",
            "99",
        ]
        assert run_computer(program, [7])[1][0] == 999
        assert run_computer(program, [8])[1][0] == 1000
        assert run_computer(program, [9])[1][0] == 1001

    def test_intcode_day_nine(self):
        program = [
            "109",
            "1",
            "204",
            "-1",
            "1001",
            "100",
            "1",
            "100",
            "1008",
            "100",
            "16",
            "101",
            "1006",
            "101",
            "0",
            "99",
        ]
        assert run_computer(program, [])[1] == list(map(int, program))

        program = ["1102", "34915192", "34915192", "7", "4", "7", "99", "0"]
        assert len(str(run_computer(program, [])[1][0])) == 16

        program = ["104", "1125899906842624", "99"]
        assert run_computer(program, [])[1][0] == 1125899906842624

        program = ["109", "6", "21001", "9", "25", "1", "104", "0", "99", "49"]
        assert run_computer(program, [])[1][0] == 74
