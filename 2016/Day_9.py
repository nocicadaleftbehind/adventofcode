import re

def part_1(line):
    current_index = 0
    length = 0
    while current_index < len(line):
        if m := re.match(r"^\((\d+)x(\d+)\)", line[current_index:]):
            group_length = int(m.group(1))    
            group_repeats = int(m.group(2))
            length += group_length * group_repeats
            current_index += len(m.group(0)) + group_length
        else:
            length += 1
            current_index += 1
    return length

def part_2(line):
    current_index = 0
    length = 0
    while current_index < len(line):
        if m := re.match(r"^\((\d+)x(\d+)\)", line[current_index:]):
            group_length = int(m.group(1))    
            group_repeats = int(m.group(2))
            before_group_index = current_index + len(m.group(0))
            length += part_2(line[before_group_index: before_group_index + group_length]) * group_repeats
            current_index += len(m.group(0)) + group_length
        else:
            length += 1
            current_index += 1
    return length

line = open("input_9.txt").read().strip()

print("PART 1")
print(part_1(line))

print("PART 2")
print(part_2(line))