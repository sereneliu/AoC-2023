import re
from re import finditer
from word2number import w2n
from aocd import get_data

puzzle_input = get_data(day=1, year=2023).split('\n')

def find_calibration(text):
    numbers = re.findall('\d', text)
    return int(numbers[0] + numbers[-1])

def find_calibration_total(doc, count_words):
    total = 0
    for line in doc:
        if count_words == False:
            total += find_calibration(line)
        else:
            total += replace_word(line)
    return total

print(find_calibration_total(puzzle_input, False))

def replace_word(text):
    numbers = []
    for num_match in finditer('\d', text):
        numbers.append((num_match.start(), int(num_match.group())))
    for key, value in w2n.american_number_system.items():
        for word_match in finditer(key, text):
            numbers.append((word_match.start(), value))
    numbers = sorted(numbers)
    return int(str(numbers[0][1]) + str(numbers[-1][1]))

print(find_calibration_total(puzzle_input, True))
