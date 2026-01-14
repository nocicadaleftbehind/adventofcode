import re
import collections

grid = collections.defaultdict(lambda: ".")
with open("input_17.txt") as file:
    for line in file:
        m = re.match("x=(\d+), y=(\d+)\.\.(\d+)", line)
        if m:
            x_start = int(m.group(1))
            x_end = int(m.group(1))
            y_start = int(m.group(2))
            y_end = int(m.group(3))
        m = re.match("y=(\d+), x=(\d+)\.\.(\d+)", line)
        if m:
            y_start = int(m.group(1))
            y_end = int(m.group(1))
            x_start = int(m.group(2))
            x_end = int(m.group(3))

        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                grid[(y, x)] = "#"

min_y = min([y for y, x in grid.keys()])
max_y = max([y for y, x in grid.keys()])
grid[(0, 500)] = "|"


def find_bound(grid, y, x, direction):
    while True:
        if grid[(y + 1, x)] in ".|":
            return False, x
        if grid[(y, x + direction)] == "|":
            return "|", x
        if grid[(y, x + direction)] in "#~":
            return True, x
        x += direction


def spawn_water(grid, source):
    while True:
        current_y, current_x = source
        if grid[(current_y, current_x)] in "~#|" and grid[(current_y + 1, current_x)] != ".":
            return

        down_stopped = False
        while current_y < max_y:
            if grid[(current_y + 1, current_x)] == "|":
                down_stopped = True
                break
            if grid[(current_y + 1, current_x)] in "~#":
                break
            current_y += 1
        if down_stopped or current_y == max_y:
            grid[(current_y, current_x)] = "|"
            continue

        left_bound, x_start = find_bound(grid, current_y, current_x, -1)
        right_bound, x_end = find_bound(grid, current_y, current_x, +1)
        if left_bound == True and right_bound == True:
            for x in range(x_start, x_end + 1):
                grid[(current_y, x)] = "~"
        if left_bound == "|" or right_bound == "|":
            for x in range(x_start, x_end + 1):
                grid[(current_y, x)] = "|"

        if not left_bound:
            spawn_water(grid, (current_y, x_start))
        if not right_bound:
            spawn_water(grid, (current_y, x_end))


spawn_water(grid, (0, 500))
counter = collections.Counter([v for k, v in grid.items() if k[0] >= min_y])

print("PART 1")
print(counter["~"] + counter["|"])

print("PART 2")
print(counter["~"])
