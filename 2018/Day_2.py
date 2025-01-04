from collections import Counter

box_ids = []
with open("input_2.txt") as file:
    for line in file:
        line = line[:-1]
        box_ids.append(line)


def part_1():
    num_twos = 0
    num_threes = 0
    for box_id in box_ids:
        counter = Counter(box_id)
        if 2 in counter.values():
            num_twos += 1
        if 3 in counter.values():
            num_threes += 1
    return num_twos * num_threes

def common(str1, str2):
    common_string = ""
    for ch1, ch2 in zip(str1, str2):
        if ch1 == ch2:
            common_string += ch1
    return common_string

def part_2():
    for box1 in box_ids:
        for box2 in box_ids:
            if box1 == box2:
                continue
            common_substring = common(box1, box2)
            if len(common_substring) == len(box1) - 1:
                return common_substring
            
print("PART 1")
print(part_1())
print("PART 2")
print(part_2())

