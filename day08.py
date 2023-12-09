from aocd import get_data
puzzle_input = get_data(day=8, year=2023).split('\n')

def fill_elements(doc):
    elements = {}
    for line in doc:
        elements[line[:3]] = (line[7:10], line[12:15])
    return elements

def escape(doc):
    instructions = doc[0]
    elements = fill_elements(doc)
    current_element = 'AAA'
    steps = 0
    while current_element != 'ZZZ':
        for instruction in instructions:
            if instruction == 'L':
                current_element = elements[current_element][0]
            elif instruction == 'R':
                current_element = elements[current_element][1]
            steps += 1
            print(instruction, current_element, steps)
    return steps

print(escape(puzzle_input))
