import re
from aocd import get_data

puzzle_input = get_data(day=3, year=2023).split('\n')


def find_part_numbers(schematic):
    sum_part_nums = 0
    for line in range(len(schematic)):
        numbers = re.finditer(r'\d+', schematic[line])
        for number in numbers:
            if check_for_symbols(schematic, line, number):
                sum_part_nums += int(number.group())
    return sum_part_nums


def check_for_symbols(schematic, line, number):
    if number.start() != 0 and schematic[line][number.start() - 1] != '.':
        return True
    if number.end() < len(schematic[line]) - 1 and schematic[line][number.end()] != '.':
        return True
    for pos in range(number.start(), number.end()):
        if line != 0:
            if schematic[line - 1][pos] != '.':
                return True
            if pos != 0 and schematic[line - 1][pos - 1] != '.':
                return True
            if pos < len(schematic[line]) - 1 and schematic[line - 1][pos + 1] != '.':
                return True
        if line < len(schematic) - 1:
            if schematic[line + 1][pos] != '.':
                return True
            if pos != 0 and schematic[line + 1][pos - 1] != '.':
                return True
            if pos < len(schematic[line]) - 1 and schematic[line + 1][pos + 1] != '.':
                return True
    return False


print(find_part_numbers(puzzle_input))
