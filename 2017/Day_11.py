with open("input_11.txt") as file:
    for line in file:
        line = line[:-1]
        directions = line.split(",")

def distance(pos):
    return (abs(pos["x"]) + abs(pos["y"]) + abs(pos["z"])) // 2


pos = {"x": 0, "y": 0, "z": 0}
max_dist = 0

for direction in directions:
    if direction == "n":
        pos["z"] -= 1
        pos["y"] += 1
    if direction == "ne":
        pos["z"] -= 1
        pos["x"] += 1
    if direction == "nw":
        pos["x"] -= 1
        pos["y"] += 1
    if direction == "s":
        pos["y"] -= 1
        pos["z"] += 1
    if direction == "se":
        pos["y"] -= 1
        pos["x"] += 1
    if direction == "sw":
        pos["x"] -= 1
        pos["z"] += 1
    max_dist = max(distance(pos), max_dist)

print("PART 1")
print(distance(pos))
print("PART 2")
print(max_dist)