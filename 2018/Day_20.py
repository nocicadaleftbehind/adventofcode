from collections import defaultdict


def move(current_position, c):
    if c == "N":
        return current_position + 1j
    if c == "S":
        return current_position - 1j
    if c == "E":
        return current_position - 1
    if c == "W":
        return current_position + 1
    return current_position


def parse_string(s):
    distances = defaultdict(int)
    current_position = 0 + 0j
    path_length = 0
    position_stack = []
    
    for c in s:
        if c in "NEWS":
            current_position = move(current_position, c)
            path_length += 1
            if current_position in distances.keys():
                path_length = min(path_length, distances[current_position])
            distances[current_position] = path_length
        elif c == "(":
            position_stack.append(current_position)
        elif c == "|":
            current_position = position_stack.pop()
            path_length = distances[current_position]
            position_stack.append(current_position)
        elif c == ")":
            position_stack.pop()
        elif c == "$":
            return distances
    return distances


with open("input_20.txt") as file:
    line = file.readline()
    distances = parse_string(line)

print("PART 1")
print(max(distances.values()))

print("PART 2")
print(len([1 for x in distances.values() if x >= 1000]))
