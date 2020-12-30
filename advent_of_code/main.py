import sys
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
import day11
import day12
import day13

days = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13]


def print_day(i):
    input = download_input(i)
    day = days[i - 1]
    print(f"Day {i} - Part 1: {day.part_one(input)}")
    print(f"Day {i} - Part 2: {day.part_two(input)}")


if len(sys.argv) == 1:
    [print_day(i + 1) for i in range(len(days))]
else:
    selected = int(sys.argv[1])
    print_day(selected)
