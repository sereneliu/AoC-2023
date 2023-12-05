import collections
from aocd import get_data

puzzle_input = get_data(day=4, year=2023).split('\n')

def find_matching(card):
    winning = set([int(n1) for n1 in card[card.index(':') + 2:card.index(' |')].split(' ') if n1 != ''])
    mine = set([int(n2) for n2 in card[card.index('|') + 2:].split(' ') if n2 != ''])
    total_winning = winning.intersection(mine)
    if len(total_winning) > 0:
        return pow(2, len(total_winning) - 1)
    else:
        return 0

def find_points(cards):
    total = 0
    for card in cards:
        total += find_matching(card)
    return total

print(find_points(puzzle_input))
