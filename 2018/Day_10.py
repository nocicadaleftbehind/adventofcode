import itertools
import re
import math

import matplotlib.pyplot as plt

points = []
with open("input_10.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        m = re.match("position=<(.+),(.+)> velocity=<(.+),(.+)>", line)
        if m:
            x_pos = int(m.group(1))
            y_pos = int(m.group(2))
            x_v = int(m.group(3))
            y_v = int(m.group(4))
        points.append((x_pos, y_pos, x_v, y_v))

best_area = math.inf
for t in itertools.count(1):
    old_points = points
    points = [(x_pos + x_v, y_pos + y_v, x_v, y_v) for (x_pos, y_pos, x_v, y_v) in points]
    x_pos = [p[0] for p in points]
    y_pos = [-p[1] for p in points]
    
    area = (max(x_pos) - min(x_pos)) * (max(y_pos) - min(y_pos))
    
    if area < best_area:
        best_area = area
    else:
        points = old_points
        x_pos = [p[0] for p in points]
        y_pos = [-p[1] for p in points]
        print("PART 2")
        print(t - 1)
        break

plt.title(f"PART 1")
plt.scatter(x_pos, y_pos)
plt.figaspect(5)
plt.show()
