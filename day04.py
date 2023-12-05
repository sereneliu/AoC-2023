import collections
from aocd import get_data

puzzle_input = get_data(day=4, year=2023).split('\n')

def find_matching(card):
    winning = set([int(n1) for n1 in card[card.index(':') + 2:card.index(' |')].split(' ') if n1 != ''])
    mine = set([int(n2) for n2 in card[card.index('|') + 2:].split(' ') if n2 != ''])
    total_winning = winning.intersection(mine)
    return len(total_winning)

def find_power(matches):
    if matches > 0:
        return pow(2, matches - 1)
    else:
        return 0

def find_points(cards):
    total = 0
    for card in cards:
        total += find_power(find_matching(card))
    return total

def find_copies(cards):
    copies = collections.defaultdict(int)
    for card in cards:
        card_num = cards.index(card) + 1
        copies[card_num] += 1
        total_matches = find_matching(card)
        for n in range(total_matches):
            copies[card_num + n + 1] += 1 * copies[card_num]
    return sum(copies.values())

print(find_points(puzzle_input))
print(find_copies(puzzle_input))
