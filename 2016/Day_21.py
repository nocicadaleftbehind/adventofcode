import itertools
import re


def swap_positions(string, pos1, pos2):
    string[pos1], string[pos2] = string[pos2], string[pos1]
    return string


def swap_letters(string, c1, c2):
    pos1 = string.index(c1)
    pos2 = string.index(c2)
    return swap_positions(string, pos1, pos2)


def rotate(string, direction, amount):
    amount = amount % len(string)
    if direction == "right":
        amount *= -1
    return string[amount:] + string[:amount]


def rotate_letter_based(string, char):
    index = string.index(char)
    if index >= 4:
        index += 1
    index += 1
    return rotate(string, "right", index)


def reverse(string, start, end):
    string[start:end + 1] = string[start:end + 1][::-1]
    return string


def move(string, pos1, pos2):
    char = string[pos1]
    string.remove(char)
    string.insert(pos2, char)
    return string


def apply_program(starting_string, program):
    scrambled_string = starting_string
    for line in program:
        m = re.match("swap position (\d+) with position (\d+)", line)
        if m:
            pos1 = int(m.group(1))
            pos2 = int(m.group(2))
            scrambled_string = swap_positions(scrambled_string, pos1, pos2)
        m = re.match("swap letter (\w+) with letter (\w+)", line)
        if m:
            c1 = m.group(1)
            c2 = m.group(2)
            scrambled_string = swap_letters(scrambled_string, c1, c2)
        m = re.match("rotate (\w+) (\d+) steps?", line)
        if m:
            direction = m.group(1)
            amount = int(m.group(2))
            scrambled_string = rotate(scrambled_string, direction, amount)
        m = re.match("rotate based on position of letter (\w+)", line)
        if m:
            char = m.group(1)
            scrambled_string = rotate_letter_based(scrambled_string, char)
        m = re.match("reverse positions (\d+) through (\d+)", line)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            scrambled_string = reverse(scrambled_string, start, end)
        m = re.match("move position (\w+) to position (\d+)", line)
        if m:
            pos1 = int(m.group(1))
            pos2 = int(m.group(2))
            scrambled_string = move(scrambled_string, pos1, pos2)
    return "".join(scrambled_string)


program = []
with open("input_21.txt") as file:
    for line in file:
        program.append(line[:-1])

print("PART 1")
print(apply_program(list("abcdefgh"), program))
for start_string in itertools.permutations("abcdefgh"):
    scrambled_string = apply_program(list(start_string), program)
    if scrambled_string == "fbgdceah":
        print("PART 2")
        print("".join(start_string))
        break
