import heapq
import numpy as np

depth = 0
target_cell = (0, 0, 1)
with open("input_22.txt") as file:
    for line in file:
        if "depth" in line:
            depth = int(line.split("depth:")[-1])
        if "target" in line:
            coords = line.split("target:")[-1].split(",")
            target_cell = (int(coords[1]), int(coords[0]), 1)


def calc_geo_types(buffer, target_cell):
    erosion_level = np.zeros((target_cell[0] + buffer + 1, target_cell[1] + buffer + 1), dtype=np.uint32)
    for y in range(len(erosion_level)):
        for x in range(len(erosion_level[0])):
            if (x, y) == target_cell[:2]:
                cell_geo_index = 0
            elif y == 0:
                cell_geo_index = x * 16807
            elif x == 0:
                cell_geo_index = y * 48271
            else:
                cell_geo_index = erosion_level[y - 1, x] * erosion_level[y, x - 1]
            erosion_level[y, x] = (cell_geo_index + depth) % 20183
    geo_type = erosion_level % 3
    return geo_type

geo_type = calc_geo_types(0, target_cell)

print("PART 1")
print(geo_type[0:target_cell[0] + 1, 0:target_cell[1] + 1].sum())

TORCH = 1
CLIMBING_GEAR = 2
NEITHER = 3

possible_gear = {0: {CLIMBING_GEAR, TORCH},
                 1: {CLIMBING_GEAR, NEITHER},
                 2: {TORCH, NEITHER}}

buffer = 0
queue = []
heapq.heappush(queue, (0, 0, 0, 0, TORCH, []))
visited = set()
while len(queue) > 0:
    current_state = heapq.heappop(queue)
    heuristic, length, x, y, current_gear, path = current_state

    if (x, y, current_gear) in visited:
        continue
    visited.add((x, y, current_gear))
    
    if x == geo_type.shape[0] - 1 or y == geo_type.shape[1] - 1:
        buffer += 10
        geo_type = calc_geo_types(buffer, target_cell)

    if (x, y, current_gear) == target_cell:
        print("PART 2")
        print(length)
        break

    current_geo_type = geo_type[x, y]
    other_gear = possible_gear[current_geo_type].difference({current_gear}).pop()
    
    if (x, y, other_gear) not in visited:
        heapq.heappush(queue, (heuristic + 7, length + 7, x, y, other_gear, path + [(x, y, other_gear)]))

    candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for candidate in candidates:
        next_x, next_y = candidate
        if not (0 <= next_x < geo_type.shape[0]):
            continue
        if not (0 <= next_y < geo_type.shape[1]):
            continue
        if (next_x, next_y, current_gear) in visited:
            continue

        next_geo_type = geo_type[next_x, next_y]
        if current_gear not in possible_gear[next_geo_type]:
            continue

        heuristic = abs(target_cell[0] - next_x) + abs(target_cell[1] - next_y)
        heapq.heappush(queue, (heuristic + length + 1, length + 1, next_x, next_y, current_gear, path + [(next_x, next_y, current_gear)]))
