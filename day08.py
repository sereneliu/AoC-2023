from aocd import get_data
puzzle_input = get_data(day=8, year=2023).split('\n')

def setup(doc):
    instructions = doc[0]
    elements = fill_elements(doc)
    return instructions, elements

def fill_elements(doc):
    elements = {}
    for line in doc:
        elements[line[:3]] = (line[7:10], line[12:15])
    return elements

def find_next(instruction, elements, element):
    if instruction == 'L':
        element = elements[element][0]
    elif instruction == 'R':
        element = elements[element][1]
    return element

def escape(doc):
    instructions, elements = setup(doc)
    current_element = 'AAA'
    steps = 0
    while current_element != 'ZZZ':
        for instruction in instructions:
            current_element = find_next(instruction, elements, current_element)
            steps += 1
    return steps

def escape_2(doc):
    instructions, elements = setup(doc)
    starting_elements = [k for k in elements.keys() if k.endswith('A')]
    ending_elements = [e for e in starting_elements if e.endswith('Z')]
    steps = 0
    while len(ending_elements) != len(starting_elements):
        for instruction in instructions:
            for idx in range(len(starting_elements)):
                starting_elements[idx] = find_next(instruction, elements, starting_elements[idx])
            print(starting_elements, ending_elements)
            steps += 1
            ending_elements = [e for e in starting_elements if e.endswith('Z')]
    return steps

print(escape_2(puzzle_input))
