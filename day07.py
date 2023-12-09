from collections import Counter
from aocd import get_data
puzzle_input = get_data(day=7, year=2023).split('\n')

labels = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
types = ['high', 'one', 'two', 'three', 'full', 'four', 'five']

def find_type(cards):
    counts = Counter(cards)
    match sorted(counts.values()):
        case [5]:
            return types.index('five')
        case [1, 4]:
            return types.index('four')
        case [2, 3]:
            return types.index('full')
        case [1, 1, 3]:
            return types.index('three')
        case [1, 2, 2]:
            return types.index('two')
        case [1, 1, 1, 2]:
            return types.index('one')
    return types.index('high')

def assign_values(hand, bet):
    hand_values = []
    hand_values.append(find_type(hand))
    card_values = []
    for card in hand:
        card_values.append(labels.index(card))
    card_values = sorted(card_values, key=card_values.count, reverse=True)
    hand_values.extend(card_values)
    hand_values.append(int(bet))
    return hand_values

def rank_and_score(all_hands):
    hands = []
    total = 0
    for hand in all_hands:
        cards, bet = hand.split(' ')
        hands.append(assign_values(cards, bet))
    hands = sorted(hands, reverse=True)
    for idx in reversed(range(len(hands))):
        total += (idx + 1) * hands[idx][-1]
    return total

print(rank_and_score(puzzle_input))
