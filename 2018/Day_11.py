import math
from collections import defaultdict

serial_number = int(open("input_11.txt").read())


def power_level(x, y):
    if x > 300 or y > 300:
        return -math.inf
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    result = int(power / 100) % 10 - 5
    return result


sum_table = defaultdict(int)
for x in range(1, 301):
    for y in range(1, 301):
        sum_table[(x, y)] = (power_level(x, y)
                             + sum_table[(x - 1, y)]
                             + sum_table[(x, y - 1)]
                             - sum_table[(x - 1, y - 1)])


def find_best_subsum(limit_size=False):
    best_coords = (0, 0, 1)
    best_power = 0

    size_range = range(1, 301)
    if limit_size:
        size_range = [3]

    for s in size_range:
        for x in range(1, 301 - s):
            for y in range(1, 301 - s):
                power = sum_table[(x, y)] - sum_table[(x + s, y)] - sum_table[(x, y + s)] + sum_table[(x + s, y + s)]
                if power >= best_power:
                    best_coords = (x + 1, y + 1, s)
                    best_power = power
    
    if limit_size:
        return f"{best_coords[0]},{best_coords[1]}"
    else:
        return f"{best_coords[0]},{best_coords[1]},{best_coords[2]}"


print("PART 1")
print(find_best_subsum(limit_size=True))
print("PART 2")
print(find_best_subsum())
