from itertools import count

depths = {}
with open("input_13.txt") as file:
    for line in file:
        line = line[:-1]
        depth, value = map(int, line.split(":"))
        depths[depth] = value


def get_severity(depths):
    total = 0
    for depth in depths.keys():
        period_at_depth = 2 * depths[depth] - 1
        if depth % (period_at_depth - 1) == 0:
            total += depth * depths[depth]
    return total

def simulate(delay, depths):
    for depth in depths.keys():
        period_at_depth = 2 * depths[depth] - 1
        if (delay + depth) % (period_at_depth - 1) == 0:
            return False
    return True

def find_start_timing(depths):
    for i in count(0):
        if simulate(i, depths):
            return i

print("PART 1")
print(get_severity(depths))
print("PART 2")
print(find_start_timing(depths))
