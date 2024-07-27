import itertools

import math

lines = []
with open("input_24.txt") as file:
    for line in file:
        line = line[:-1]
        lines.append(line)

def find_numbers(lines):
    number_pos = {}
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char != "#" and char != ".":
                number_pos[char] = (x,y)
    return number_pos

def calc_neighbors(pos):
    x,y = pos
    neighbors = []
    for (i,j) in [(-1, 0), (1,0), (0,-1), (0,1)]:
        new_x = x + i
        new_y = y + j
        if lines[new_x][new_y] != "#":
            neighbors.append((new_x, new_y))
    return neighbors

def calc_length(start, startchar, end, number_positions, lengths, max_length):
    if (startchar, end) in lengths.keys():
        return lengths[(startchar, end)]

    queue = [(0, start)]
    visited = []
    while True:
        length, pos = queue.pop(0)
        if length >= max_length:
            return max_length
        if pos == number_positions[end]:
            lengths[(startchar, end)] = length
            return length
        if pos in visited:
            continue
        visited.append(pos)
        for n in calc_neighbors(pos):
            if n in visited:
                continue
            queue.append((length + 1, n))

def find_shortest_permutation(return_to_start = False):
    number_positions = find_numbers(lines)
    lengths = {}
    min_length = math.inf
    
    for route in itertools.permutations([c for c in number_positions.keys() if c != "0"]):
        route = list(route)
        route.insert(0, "0") 

        if return_to_start:
            route.append("0")
    
        total_length = 0
        for (start, end) in zip(route, route[1:]):
            start_pos = number_positions[start]
            total_length += calc_length(start_pos, start, end, number_positions, lengths, min_length - total_length)
            if total_length > min_length:
                break
        min_length = min(min_length, total_length)
    
    return min_length

print("PART 1")
print(find_shortest_permutation())
print("PART 2")
print(find_shortest_permutation(True))
