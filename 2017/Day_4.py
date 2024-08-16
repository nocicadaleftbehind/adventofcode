lines = []
with open("input_4.txt") as file:
    for line in file:
        line = line[:-1]
        lines.append(line)


def part_1(lines):
    num_valid = 0
    for line in lines:
        words = line.split(" ")
        if len(words) == len(set(words)):
            num_valid += 1
    return num_valid


def part_2(lines):
    num_valid = 0
    for line in lines:
        words = line.split(" ")
        new_words = []
        for word in words:
            word = "".join(sorted(word))
            new_words.append(word)
        if len(words) == len(set(new_words)):
            num_valid += 1
    return num_valid


print("PART 1")
print(part_1(lines))
print("PART 2")
print(part_2(lines))
