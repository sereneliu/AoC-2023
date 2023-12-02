import re
from aocd import get_data

puzzle_input = get_data(day=2, year=2023).split('\n')

games = {}

def parse_data(data):
    for game in data:
        key, value = game.split(':')
        game_number = int(key[key.index(' ') + 1:])
        games[game_number] = []

        game_sets = value.split(';')
        for game_set in game_sets:
            # re.search('(?:^|, )(\d+)(?: blue)', game_set)
            colors = [0, 0, 0]
            unsorted_colors = game_set.split(',')
            for color in unsorted_colors:
                if re.search('blue', color):
                    colors[0] = int(color[:color.index(' blue')].strip())
                elif re.search('green', color):
                    colors[1] = int(color[:color.index(' green')].strip())
                elif re.search('red', color):
                    colors[2] = int(color[:color.index(' red')].strip())
            games[game_number].append(colors)

parse_data(puzzle_input)

def find_max(colors):
    blues = []
    greens = []
    reds = []
    for game_set in colors:
        blues.append(game_set[0])
        greens.append(game_set[1])
        reds.append(game_set[2])
    return max(blues), max(greens), max(reds)

def find_possible(game_key, game_value, max_blue, max_green, max_red):
    max_blues, max_greens, max_reds = find_max(game_value)
    if max_blue >= max_blues and max_green >= max_greens and max_red >= max_reds:
        return game_key
    else:
        return 0

def find_game_id_sum(game_dict):
    game_id_sum = 0
    for key, value in game_dict.items():
        game_id_sum += find_possible(key, value, 14, 13, 12)
    return game_id_sum

def part_two(game_dict):
    power_sum = 0
    for key, value in game_dict.items():
        b, g, r = find_max(value)
        power = b * g * r
        power_sum += power
    return power_sum

print(find_game_id_sum(games))
print(part_two(games))
