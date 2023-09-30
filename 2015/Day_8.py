def part_1(line):
    return len(eval(line))

def part_2(line):
    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    line = '"' + line + '"'
    return len(line)

print("PART 1")
print(part_1('""'), 0)
print(part_1('"abc"'), 3)
print(part_1('"aaa\\"aaa"'), 7)
print(part_1('"\x27"'), 1)

print("PART 2")
print(part_2('""'), 6)
print(part_2('"abc"'), 9)
print(part_2('"aaa\\"aaa"'), 16)
print(part_2('"\\x27"'), 11)

num_chars = 0
num_chars_evaluated = 0
num_chars_for_representation = 0
with open("input_8.txt") as file:
    for line in file:
        line = line[:-1]
        num_chars += len(line)
        num_chars_evaluated += part_1(line)
        num_chars_for_representation += part_2(line)

print(num_chars - num_chars_evaluated)
print(num_chars_for_representation - num_chars)
