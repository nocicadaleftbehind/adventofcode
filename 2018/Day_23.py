import re

import numpy as np

nanobots = []
with open("input_23.txt") as file:
    for line in file:
        if m := re.match("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", line):
            x = int(m.group(1))
            y = int(m.group(2))
            z = int(m.group(3))
            radius = int(m.group(4))
            nanobots.append((x, y, z, radius))


def distance(p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(3))


num_bots = len(nanobots)
best_bot = np.argmax([nanobots[i][3] for i in range(num_bots)])
best_radius = nanobots[best_bot][3]
num_in_range = len([n for n in nanobots if distance(n, nanobots[best_bot]) < best_radius])

print("PART 1")
print(int(num_in_range))

FINAL_GRID_SIZE = 16


def next_power_of_two(i):
    n = 1
    while n < i:
        n *= 2
    return n


def get_round_intervalls(x):
    return min(x) - max_r, min(x) - max_r + next_power_of_two(max(x) - min(x) + 2 * max_r)


max_r = max([n[3] for n in nanobots])
bounds = [get_round_intervalls([n[i] for n in nanobots]) for i in range(3)]

num_round = 0
while True:
    grid = np.zeros((2, 2, 2))
    min_x, max_x = bounds[0]
    min_y, max_y = bounds[1]
    min_z, max_z = bounds[2]

    if max_x - min_x <= FINAL_GRID_SIZE and max_y - min_y <= FINAL_GRID_SIZE and max_z - min_z <= FINAL_GRID_SIZE:
        break

    for i in range(num_bots):
        bot_presence = np.zeros((2, 2, 2))
        x, y, z, r = nanobots[i]
        for cx, cy, cz in [(x - r, y, z), (x + r, y, z),
                           (x, y - r, z), (x, y + r, z),
                           (x, y, z - r), (x, y, z + r)]:
            if cx < min_x or cx > max_x or cy < min_y or cy > max_y or cz < min_z or cz > max_z:
                continue
            ix = int(cx > min_x + (max_x - min_x) // 2)
            iy = int(cy > min_y + (max_y - min_y) // 2)
            iz = int(cz > min_z + (max_z - min_z) // 2)
            bot_presence[ix, iy, iz] = 1
        grid += bot_presence

    max_box = np.unravel_index(grid.argmax(), grid.shape)
    min_bound, max_bound = bounds[num_round % 3]
    if max_bound - min_bound > FINAL_GRID_SIZE:
        half_point = min_bound + (max_bound - min_bound) // 2
        if max_box[num_round % 3] == 0:
            max_bound = half_point
        else:
            min_bound = half_point
        bounds[num_round % 3] = (min_bound, max_bound)

    num_round += 1

# brute force check the final grid
in_range = np.zeros((FINAL_GRID_SIZE, FINAL_GRID_SIZE, FINAL_GRID_SIZE))
best_coord = None
best_in_range = 0
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        for z in range(min_z, max_z):
            num_in_range = len([n for n in nanobots if distance(n, (x, y, z)) <= n[3]])
            if num_in_range > best_in_range:
                best_coord = (x, y, z)
                best_in_range = num_in_range

print("PART 2")
print(distance((0, 0, 0), best_coord))
