import itertools

spreadsheet = []
with open("input_2.txt") as file:
    for line in file:
        line = line[:-1]
        spreadsheet.append(list(map(int, line.split("\t"))))


def part_1(spreadsheet):
    checksum = 0
    for line in spreadsheet:
        checksum += max(line) - min(line)
    return checksum


def part_2(spreadsheet):
    checksum = 0
    for line in spreadsheet:
        for a, b in itertools.product(line, line):
            if a <= b:
                continue
            if a % b == 0:
                checksum += a // b
                break
    return checksum


print(part_1(spreadsheet))
print(part_2(spreadsheet))
