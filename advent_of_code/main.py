import sys
from lib.get_input import download_input
import day1
import day2
import day3
import day4
import day5

days = [day1, day2, day3, day4, day5]


def print_day(i):
    input = download_input(i)
    day = days[i - 1]
    print(f'Day {i} - Part 1: {day.part_one(input)}')
    print(f'Day {i} - Part 2: {day.part_two(input)}')


if (len(sys.argv) == 1):
    [print_day(i + 1) for i in range(len(days))]
else:
    selected = int(sys.argv[1])
    print_day(selected)
