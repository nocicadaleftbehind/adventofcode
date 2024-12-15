import copy
from collections import defaultdict

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

infected = defaultdict(int)
with open("input_22.txt") as file:
    for index, line in enumerate(file):
        line = line[:-1]
        for c_index, c in enumerate(line):
            status = CLEAN
            if c == "#":
                status = INFECTED
            infected[(c_index, index)] = status

max_x = max([x for (x, y) in infected.keys()])
max_y = max([y for (x, y) in infected.keys()])

            
def cell_index(pos):
    return int(pos.real), int(pos.imag)

def part_1(infected):
    infected = copy.deepcopy(infected)
    current_position = max_x // 2 + max_y // 2 * 1j
    current_orientation = 0 - 1j
    num_infections = 0
    for i in range(10000):
        cell_status = infected[cell_index(current_position)]

        if cell_status == CLEAN:
            current_orientation *= -1j
            infected[cell_index(current_position)] = INFECTED
            num_infections += 1
        elif cell_status == INFECTED:
            current_orientation *= 1j
            infected[cell_index(current_position)] = CLEAN

        current_position += current_orientation

    return num_infections

def part_2(infected):
    infected = copy.deepcopy(infected)
    current_position = max_x//2 + max_y//2 * 1j
    current_orientation = 0 - 1j
    num_infections = 0
    for i in range(10000000):
        cell_status = infected[cell_index(current_position)]
    
        if cell_status == CLEAN:
            current_orientation *= -1j
            infected[cell_index(current_position)] = WEAKENED
        elif cell_status == WEAKENED:
            num_infections += 1
            infected[cell_index(current_position)] = INFECTED
        elif cell_status == INFECTED:
            current_orientation *= 1j
            infected[cell_index(current_position)] = FLAGGED
        elif cell_status == FLAGGED:
            current_orientation *= -1
            infected[cell_index(current_position)] = CLEAN
    
        current_position += current_orientation
    
    return num_infections

print("PART 1")
print(part_1(infected))
print("PART 2")
print(part_2(infected))