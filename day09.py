from aocd import get_data
puzzle_input = get_data(day=9, year=2023).split('\n')

def find_difference(history):
    difference = []
    for idx in range(len(history) - 1):
        difference.append(history[idx + 1] - history[idx])
    return difference

def find_next_value(history):
    difference = history
    first_values = [difference[0]]
    last_value = history[-1]
    while set(difference) != {0}:
        difference = find_difference(difference)
        first_values.append(difference[0])
        last_value += difference[-1]
    first_value = first_values[-1]
    while len(first_values) >= 2:
        first_value = first_values[-2] - first_value
        first_values.pop()
    return first_value, last_value

def find_sum(dataset):
    part_1_sum = 0
    part_2_sum = 0
    for history in dataset:
        history = [int(x) for x in history.split(' ')]
        part_1_sum += find_next_value(history)[0]
        part_2_sum += find_next_value(history)[1]
    return part_1_sum, part_2_sum

print(find_sum(puzzle_input))
