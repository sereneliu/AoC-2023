import re
from aocd import get_data
puzzle_input = get_data(day=1, year=2023).split('\n')

def find_calibration(text):
    numbers = re.findall('\d', text)
    return int(numbers[0] + numbers[-1])

def find_calibration_total(doc):
    total = 0
    for line in doc:
        total += find_calibration(line)
    return total

print(find_calibration_total(puzzle_input))
