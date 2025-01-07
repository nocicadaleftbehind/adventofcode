import numpy as np
import re

lines = []
with open("input_3.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        lines.append(line)

patches = []
for line in lines:
    m = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    if m:
        claim_num = int(m.group(1))
        start_x = int(m.group(2))
        start_y = int(m.group(3))
        x_size = int(m.group(4))
        y_size = int(m.group(5))
        patches.append((claim_num, start_x, start_y, x_size, y_size))

grid = np.zeros((1000, 1000), dtype=np.uint8)
for patch in patches:
    claim_num, start_x, start_y, x_size, y_size = patch
    grid[start_x:start_x+x_size, start_y:start_y+y_size] += 1
print("PART 1")
print((grid > 1).sum())

print("PART 2")
for patch in patches:
    claim_num, start_x, start_y, x_size, y_size = patch
    if (grid[start_x:start_x + x_size, start_y:start_y + y_size] > 1).sum() == 0:
        print(claim_num)
        