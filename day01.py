import re
from word2number import w2n
from aocd import get_data

puzzle_input = get_data(day=1, year=2023)

def find_calibration(text):
    numbers = re.findall('\d', text)
    return int(numbers[0] + numbers[-1])

def find_calibration_total(doc):
    total = 0
    for line in doc.split('\n'):
        total += find_calibration(line)
    return total

print(find_calibration_total(puzzle_input))

def replace_word(doc):
    new_doc = doc
    for num_word, num_int in w2n.american_number_system.items():
        new_doc = re.sub(num_word, str(num_int), new_doc, re.M)
    return new_doc

print(find_calibration_total(replace_word(puzzle_input)))
