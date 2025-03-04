from collections import Counter

import numpy as np

points = []
with open("input_6.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        
        coords = line.split(",")
        x = int(coords[0])
        y = int(coords[1])
        points.append((x,y))

GRID_SIZE = max(max(x) for x in points)

def part_1():
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.int8)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            distances = [abs(x - p_x) + abs(y - p_y) for p_x, p_y in points]
            min_dist = min(distances)
            if distances.count(min_dist) == 1:
                grid[x][y] = distances.index(min_dist)
            else:
                grid[x][y] = -1

    c = Counter(grid.flatten())
    del c[-1]
    for b in range(GRID_SIZE):
        del c[grid[b][0]]
        del c[grid[b][GRID_SIZE - 1]]
        del c[grid[0][b]]
        del c[grid[GRID_SIZE - 1][b]]
    return max(c.values())

def part_2():
    count = 0
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            total_dist = sum([abs(x - p_x) + abs(y - p_y) for p_x, p_y in points])
            if total_dist < 10000:
                count +=1
    return count

print("PART 1")
print(part_1())
print("PART 2")
print(part_2())