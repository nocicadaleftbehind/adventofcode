import copy

lines = []
with open("input_5.txt") as file:
    for line in file:
        line = int(line[:-1])
        lines.append(line)


def part_1(jump_offsets):
    jump_offsets = copy.copy(jump_offsets)
    index = 0
    num_steps = 0
    while True:
        offset = jump_offsets[index]
        next_index = index + offset
        num_steps += 1
        jump_offsets[index] += 1
        index = next_index
        if index < 0 or index >= len(jump_offsets):
            return num_steps
        
def part_2(jump_offsets):
    jump_offsets = copy.copy(jump_offsets) 
    index = 0
    num_steps = 0
    while True:
        offset = jump_offsets[index]
        next_index = index + offset
        num_steps += 1
        if offset >= 3:
            jump_offsets[index] -= 1
        else:
            jump_offsets[index] += 1
        index = next_index
        if index < 0 or index >= len(jump_offsets):
            return num_steps

print("PART 1")
print(part_1(lines))
print("PART 2")
print(part_2(lines))
