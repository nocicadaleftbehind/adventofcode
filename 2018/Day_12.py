import itertools
import re

survival_rules = set()
initial_state = []
with open("input_12.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        m = re.match("initial state: (.+)", line)
        if m:
            initial_state = m.group(1)
        m = re.match("(.+) => #", line)
        if m:
            condition = m.group(1)
            survival_rules.add(condition)

def get_neighbors(grid, index):
    result = ""
    for i in range(index - 2, index + 3):
        if i in grid:
            result += "#"
        else:
            result += "."
    return result

def calc_new_grid(grid):
    new_grid = []
    min_border = min(grid) - 4
    max_border = max(grid) + 4
    for k in range(min_border, max_border+1):
        surroundings = get_neighbors(grid, k)
        if surroundings in survival_rules:
            new_grid.append(k)
    return new_grid

def part_1():
    grid = [i for i, c in enumerate(initial_state) if c == "#"]

    for i in range(20):
        grid = calc_new_grid(grid)
    return sum(grid)

def part_2(limit):
    grid = [i for i, c in enumerate(initial_state) if c == "#"]

    diffs = [0]
    last_grid_sum = 0
    for i in itertools.count(1):
        grid = calc_new_grid(grid)
        grid_sum = sum(grid)
        diffs.append(grid_sum - last_grid_sum)
        last_grid_sum = grid_sum
        if len(set(diffs[-10:])) == 1:
            return sum(grid) + diffs[-1] * (limit - i)

print("PART 1")
print(part_1())
print("PART 2")
print(part_2(50 * 10**9))