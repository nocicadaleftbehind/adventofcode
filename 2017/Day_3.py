import math
from collections import defaultdict

input_value = int(open("input_3.txt").read())


def layer(n):
    return math.ceil((math.sqrt(n) - 1) / 2)


def straight_lines(l):
    lower_right = (2 * l + 1) ** 2
    return [lower_right - k * l for k in [1, 3, 5, 7]]


def part_1(n):
    l = layer(n)
    return l + min([abs(n - x) for x in straight_lines(l)])


def next_coords(x, y):
    if y > -x and x > y:
        return x, y + 1
    if y > -x and y >= x:
        return x - 1, y
    if y <= -x and x < y:
        return x, y - 1
    if y <= -x and x >= y:
        return x + 1, y
    return x, y


def get_neighbors(pos_x, pos_y):
    return [(pos_x - 1, pos_y - 1), (pos_x - 1, pos_y), (pos_x - 1, pos_y + 1),
            (pos_x, pos_y - 1), (pos_x, pos_y), (pos_x, pos_y + 1),
            (pos_x + 1, pos_y - 1), (pos_x + 1, pos_y), (pos_x + 1, pos_y + 1)]


def part_2(n):
    values = defaultdict(int)
    pos_x, pos_y = 0, 0
    values[(pos_x, pos_y)] = 1
    while True:
        pos_x, pos_y = next_coords(pos_x, pos_y)
        sum_values = sum([values[x, y] for x, y in get_neighbors(pos_x, pos_y)])
        values[(pos_x, pos_y)] = sum_values
        if sum_values >= n:
            return sum_values


print("PART 1")
print(part_1(input_value))
print("PART 2")
print(part_2(input_value))
