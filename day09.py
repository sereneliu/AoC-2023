from aocd import get_data
puzzle_input = get_data(day=9, year=2023).split('\n')

def find_difference(history):
    difference = []
    for idx in range(len(history) - 1):
        difference.append(history[idx + 1] - history[idx])
    return difference

def find_next_value(history):
    difference = history
    last_value = history[-1]
    while set(difference) != {0}:
        difference = find_difference(difference)
        last_value += difference[-1]
    return last_value

def find_sum(dataset):
    sum = 0
    for history in dataset:
        history = [int(x) for x in history.split(' ')]
        sum += find_next_value(history)
    return sum

print(find_sum(puzzle_input))
